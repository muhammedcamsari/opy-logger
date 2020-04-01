# Opy-logger

Opy-logger, uygulamalar için günlük kaydı tutmanıza imkan tanıyan Python kütüphanesidir.


# Kurulumu

Opy-logger kurulumu için pip deposunu kullanabilirsiniz. 

	pip install opy-logger


# Kullanımı

Opy-logger kullanımı için Wiki sayfasını inceleyebilirsiniz. Size en iyi bilgiyi [Wiki](https://github.com/muhammedcamsari/opy-logger/wiki) sunar!


# 2.x sürümündeki değişiklikler

Bu sürümde, günlük kaydı tutma özelliğini ekledim. Artık çıktılar dosyaya yazılabilecek. 1.x serisi, bu özelliği desteklemiyordu.

Opy-logger, bu sürüm itibariyle yerelleştirmeyi destekliyor. Bu yüzden çıktı kategorilerindeki metinleri türkçeleştirdim. İngilizce, Fransızca, Almanca ve Rusça dil desteği yakında eklenecek. 

init() argümanını bu sürümde kaldırdım, yerine appinfo() argümanını ekledim. Artık kütüphaneniz yada uygulamanız hakkında bilgi vermek istediğinizde appinfo() kullanmalısınız. Bu argümanı kullanırken satır tipini belirlemelisiniz. (satır ve boşluk destekler) Üstelik E-Mail, lisans gibi bilgileri de destekliyor.

Artık loglardaki tarih görünürlüğünü tek bir argüman ile belirleyebiliyorsunuz. Satır sonuna date=False ifadesini eklemek zorunda değilsiniz.

Renklendirme seçeneğini de atlamadım. Artık tek bir argüman ile renklendirmeyi kapatabiliyorsunuz.

2.1 sürümüyle birlikte gizlenebilen çıktılar özelliğini ekledik. Bu özellik sayesinde çıktılar ekrana yazdırılmadan log dosyasına yazılabilecek.


# Destek Ver

opy-logger modülünü kullanmak en büyük desteğinizdir. Geribildirimler için muhammedcamsari@icloud.com mail adresini kullanabilirsiniz.