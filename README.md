# Opy-Logger

OpenSSL-GTK uygulamasında kullanmak üzere geliştirilmiştir. Bu sürümde çıktılar log dosyasına kayıt edilmez. Şimdilik planlanan bir özelliktir.

## Opy-Logger Kurulumu

Aşağıdaki komutu uçbirimde çalıştırarak kurulumu yapabilirsiniz.

	pip install opy-logger

## Opy-Logger Kullanımı

Aşağıdaki komut ile modül çağırılır.

	import opylogger 

### init() 

Bu fonksiyon, geliştirilen uygulama hakkında bilgi vermek için kullanılır. 

	init(name=None, version=None, author=None, url=None)

 - name: Uygulamanın Adı
 - version: Uygulamanın Sürümü
 - author: Uygulamanın yazarı/geliştiricisi
 - url: Uygulamanın web sitesi

Kullanımı aşağıdaki gibidir.

 	opylogger.init('X Uygulaması', '2.13.1', 'XX', 'github.com/xxx')

 Ya da

 	opylogger.init(name='X Uygulaması', version='2.13.1', author='XX', url='github.com/xxx')

Çıktısı aşağıdaki gibidir.

	>>> opylogger.init('OpyLogger', '1.0', 'Muhammed Çamsarı', 'github.com/muhammedcamsari')
	--- App Info -----------------------
	Name: OpyLogger Version: 1.0 Author: Muhammed Çamsarı Website: github.com/muhammedcamsari

### sysinfo()

 Bu fonksiyon, sistem hakkında bilgi verir. Herhangi bir argüman gerektirmez.

 	sysinfo()

 Kullanımı aşağıdaki gibidir.

 	opylogger.sysinfo()

 Çıktısı aşağıdaki gibidir.

	>>> opylogger.sysinfo()
	--- System Info --------------------
	OPY-Logger Version: 1.0
	System: Darwin
	Machine: x86_64
	Python: 3.7.3
	Compiler: Clang 10.0.1 (clang-1001.0.46.3)


### moduleinfo()

Opy-Logger modulü ile ilgili bilgiler verir.

	moduleinfo()

Çıktısı aşağıdaki gibidir.

	>>> opylogger.moduleinfo()
	--- Module Info --------------------
	Name: OPY-Logger
	Version: 1.0Beta
	Author: Muhammed Çamsarı
	License: MIT License
	Support: muhammedcamsari@icloud.com
	Copyright (c) 2019 Muhammed Çamsarı

### error()

Hata mesajlarını belirtmek için kullanılan fonksiyondur.

	error(message, category=None, date=True)

 - message: Hata mesajı
 - category: Hata mesajı ile ilgili kategori
 - date: Çıktıda tarih ve saatin görünmesi

Kullanımı aşağıdaki gibidir.

	opylogger.error('Dosya okunamadı')

Ya da 

	opylogger.error('Dosya okunamadı', 'DOSYA', False)

Ya da

	opylogger.error(message='Dosya Okunamadı', category='DOSYA', date=True)

Çıktısı aşağıdaki gibidir.

	>>> opylogger.error(message='Dosya Okunamadı', category='DOSYA', date=True)
	2019-07-10 17:32:58.794032 [ERROR] [DOSYA] Dosya Okunamadı


### critical()

Kritik uyarıları belirtmek için kullanılan fonksiyondur.

	critical(message, category=None, date=True)

 - message: Hata mesajı
 - category: Hata mesajı ile ilgili kategori
 - date: Çıktıda tarih ve saatin görünmesi

Kullanımı aşağıdaki gibidir.
	
	opylogger.critical('Dosya yok?')

Ya da

	opylogger.critical('Dosya yok?', 'DOSYA', False)

Ya da

	opylogger.critical(message='Dosya yok?', category='DOSYA', date=True)

Çıktısı aşağıdaki gibidir.

	>>> opylogger.critical(message='Dosya yok?', category='DOSYA', date=True)
	2019-07-10 17:38:37.831036 [CRITICAL] [DOSYA] Dosya yok?

### debug()

Hata ayıklama mesajlarını belirtmek için kullanılan fonksiyondur.

	debug(message, category=None, date=True)

 - message: Hata mesajı
 - category: Hata mesajı ile ilgili kategori
 - date: Çıktıda tarih ve saatin görünmesi

Kullanımı aşağıdaki gibidir.

	opylogger.debug('Dosya varmış yanlış yere bakılmış')

Ya da

	opylogger.debug('Dosya varmış yanlış yere bakılmış', 'DOSYA', False)

Ya da

	opylogger.debug('Dosya varmış yanlış yere bakılmış', category='DOSYA', date=True)

Çıktısı aşağıdaki gibidir.

	>>> opylogger.debug('Dosya varmış yanlış yere bakılmış', category='DOSYA', date=True)
	2019-07-10 17:41:48.251486 [DEBUG] [DOSYA] Dosya varmış yanlış yere bakılmış


### warning()

Uyarı mesajlarını belirtmek için kullanılan fonksiyondur.

	warning(message, category=None, date=True)

 - message: Hata mesajı
 - category: Hata mesajı ile ilgili kategori
 - date: Çıktıda tarih ve saatin görünmesi

Kullanımı aşağıdaki gibidir.

	opylogger.warning('Dosya kaybolmuş olabilir?!')

Ya da

	opylogger.warning('Dosya kaybolmuş olabilir?!', 'DOSYA', False)

Ya da

	opylogger.warning('Dosya kaybolmuş olabilir?!', category='DOSYA', date=True)

Çıktısı aşağıdaki gibidir.

	>>> opylogger.warning('Dosya kaybolmuş olabilir?!', category='DOSYA', date=True)
	2019-07-10 17:44:40.784462 [WARNING] [DOSYA] Dosya kaybolmuş olabilir?!


### info()
Bilgi mesajları için kullanılan fonksiyondur.


	info(message, category=None, date=True)

 - message: Hata mesajı
 - category: Hata mesajı ile ilgili kategori
 - date: Çıktıda tarih ve saatin görünmesi

Kullanımı aşağıdaki gibidir.

	opylogger.info('Bilgiyi verdim')

Ya da

	opylogger.info('Bilgiyi verdim', category='DOSYA', date=True)

Ya da

	opylogger.info('Bilgiyi verdim', category='DOSYA', date=True)

Çıktısı aşağıdaki gibidir.

	>>> opylogger.info('Bilgiyi verdim', category='DOSYA', date=True)
	2019-07-10 17:46:43.486754 [INFO] [DOSYA] Bilgiyi verdim

