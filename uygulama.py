import re
from pathlib import Path

YAS_GRUPLARI = {"1": "18–29", "2": "30–49", "3": "50+"}


def secim_al(soru, secenekler):
    # Geçersiz bir seçimde yalnızca bu soruyu tekrarla.
    while True:
        secim = input(soru).strip()
        if secim in secenekler:
            return secim
        print("Listeden geçerli bir seçenek seç.")


def kayit_al(kayitlar):
    kayitli_kodlar = {kayit["kod"] for kayit in kayitlar}
    while True:
        kod = input("Katılımcı kodu (ör. K015): ").strip().upper()
        if not kod:
            print("Katılımcı kodu boş bırakılamaz.")
        # DUZELTME: Katılımcı kodu alanında ad gibi serbest metinleri reddet.
        elif not re.fullmatch(r"K[0-9]{3}", kod):
            print("K harfinden sonra üç rakam gir. Örnek: K015.")
        # DUZELTME: Aynı kodun raporda iki farklı durumda görünmesini engelle.
        elif kod in kayitli_kodlar:
            print("Bu kod zaten kayıtlı. Başka bir kod gir.")
        else:
            break

    yas = secim_al("Yaş grubu (1: 18–29, 2: 30–49, 3: 50+): ", YAS_GRUPLARI)
    durum = secim_al("Durum (1: Tamamlandı, 2: Takip bekliyor): ", ("1", "2"))
    sure = None
    # Takip bekleyen kayıt için süre sorusunu atla.
    if durum == "1":
        while True:
            try:
                sure = int(input("Süre (dakika): "))
            except ValueError:
                sure = 0
            if sure > 0:
                break
            print("Süreyi 1 veya daha büyük bir tam sayı olarak gir.")

    return {"kod": kod, "yas": yas, "durum": durum, "sure": sure}


def rapor_hazirla(kayitlar):
    tamamlanan = dict.fromkeys(YAS_GRUPLARI, 0)
    takip = []
    for kayit in kayitlar:
        if kayit["durum"] == "1":
            tamamlanan[kayit["yas"]] += 1
        else:
            takip.append(kayit["kod"])

    satirlar = ["SAHA GÖRÜŞMESİ ÖZETİ", "", "Tamamlanan görüşmeler"]
    for secim, etiket in YAS_GRUPLARI.items():
        satirlar.append(f"{etiket:>5} yaş | {tamamlanan[secim]}")
    satirlar.append("")
    satirlar.append("Takip bekleyenler (henüz görüşülmedi)")
    satirlar.append(", ".join(takip) if takip else "Yok")
    return "\n".join(satirlar) + "\n"


def main():
    kayitlar = []
    while True:
        secim = secim_al("1: Kayıt ekle, 2: Raporu göster: ", ("1", "2"))
        if secim == "1":
            kayitlar.append(kayit_al(kayitlar))
        elif kayitlar:
            break
        else:
            # DUZELTME: Boş bir rapor önceki raporun üzerine yazılmasın.
            print("Henüz kayıt yok. Önce bir görüşme kaydı ekle.")

    rapor = rapor_hazirla(kayitlar)
    print("\n" + rapor, end="")
    try:
        Path("saha_ozeti.txt").write_text(rapor, encoding="utf-8")
    except OSError:
        print("Rapor dosyaya kaydedilemedi.")
    else:
        print("Rapor saha_ozeti.txt dosyasına kaydedildi.")


if __name__ == "__main__":
    main()
