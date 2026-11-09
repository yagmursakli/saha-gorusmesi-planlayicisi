# Yapay zekâ ile çalışma günlüğü

## 1. Girdi akışı

> Saha Görüşmesi Planlayıcısı için veri giriş akışını tasarla. Özellikle görüşme tamamlandıysa sürenin nasıl doğrulanacağını, görüşme hâlâ takip bekliyorsa süre sorusunun nasıl ele alınacağını örneklerle açıkla. Kodlamaya geçmeden önce takip bekleyen kayıtlar için iki seçenek öner.

**YZ yanıtı** — ChatGPT, takip bekleyen kayıtta süre sorusunu atlamayı veya 0 istemeyi önerdi.

**Karar ve gerekçe** — Kabul ettim. Görüşme yapılmadığında süre girmek gereksiz. Soruyu atlamak veri girişini kolaylaştırıyor.

**Uygulama ve test** — Süre yalnızca tamamlanan görüşmeler için soruldu.

## 2. Tekrarlanan kod

> Saha Görüşmesi Planlayıcısı’nın ilk Python sürümünü yaz ve çalıştır. Program katılımcı kodunu, yaş grubunu ve görüşme durumunu doğrulasın. Süreyi yalnızca tamamlanmış görüşmelerde sorsun. Veri girişi bitince yaş gruplarına göre tamamlanan görüşme sayılarını ve takip bekleyen katılımcı kodlarını ekrana yazıp özeti `.txt` dosyasına kaydetsin. Bir tamamlanmış ve bir takip bekleyen görüşme girerek sonucu test et. Aynı katılımcı kodu ikinci kez girilirse ilk sürümün ne yaptığını da dene ve tekrar eden kodları ele almak için iki seçenek öner.

**YZ yanıtı** — İlk sürüm K001 ve k001 girdilerini ayrı kayıt olarak kabul etti. Aynı katılımcı iki farklı durumda rapora girdi.

**Karar ve gerekçe** — Düzenledim. Aynı kişinin raporda iki kez görünmesini önlemek ve önceki kaydı korumak istedim.

**Uygulama ve test** — Tekrar eden kod reddedildi. Yeniden testte k001 reddedildi ve K014 kabul edildi.

## 3. Boş rapor

> Saha Görüşmesi Planlayıcısı’nın güncel sürümünü hatalı girdilerle çalıştır. Katılımcı kodunu boş bırakmayı, listede olmayan bir yaş grubu seçmeyi ve tamamlanmış bir görüşme için `0` ya da `2,5` dakika girmeyi dene. Her denemede beklenen sonucu ve programın gerçekte ne yaptığını tabloya yaz. Ayrıca hiç kayıt eklemeden rapor istendiğinde ne olduğunu test et ve bu durum için iki seçenek öner.

**YZ yanıtı** — Hatalı alanların yeniden sorulduğu doğrulandı. İlk davranışta boş oturum tüm değerleri sıfır gösteren dosya yazıyordu.

**Karar ve gerekçe** — Düzenledim. Yanlışlıkla rapor istediğimde önceki raporun üzerine boş bir rapor yazılmasını istemedim.

**Uygulama ve test** — Kayıt yoksa menüye dönülüyor. Mevcut dosyanın bu durumda korunduğu test edildi.

## 4. Dosya adı

> Saha Görüşmesi Planlayıcısı’nı iki ayrı oturumda çalıştır. Her oturumda farklı bir görüşme kaydı gir ve ikisini de aynı klasöre kaydet. İkinci geçerli raporun ilk rapora ne yaptığını kontrol et. Tek bir güncel rapor tutmak ile her oturumun raporunu ayrı dosyada saklamak arasındaki farkı açıkla ve iki seçenek sun.

**YZ yanıtı** — Aynı klasördeki iki geçerli oturumun ikincisi ilk raporun üzerine yazdı. ChatGPT numaralı dosyalar da önerdi.

**Karar ve gerekçe** — Kabul ettim. En güncel raporu her seferinde aynı dosyada bulmak istedim.

**Uygulama ve test** — saha_ozeti.txt adı korundu.

## 5. Katılımcı kodunun biçimi

> Saha Görüşmesi Planlayıcısı’nda katılımcı kodu alanına `K015` ve `Ornek Kisi` gibi hayalî girdiler yazarak programı test et. Hangilerinin kabul edildiğini ve takip listesine nasıl yazıldığını göster. Katılımcı adı gibi bilgilerin yanlışlıkla rapora girmesini azaltmak için iki basit kod kuralı öner. Her kural için geçerli ve geçersiz birer örnek ver.

**YZ yanıtı** — Testte ilk kod kuralı Ornek Kisi girdisini kabul etti ve rapora ORNEK KISI yazdı.

**Karar ve gerekçe** — Düzenledim. Kodların aynı biçimde olmasını ve yanlışlıkla girilen isimlerin rapora yazılmamasını istedim.

**Uygulama ve test** — K ve üç rakam kuralı eklendi. Ornek Kisi ve K15 reddedildi, k015 kabul edildi.
