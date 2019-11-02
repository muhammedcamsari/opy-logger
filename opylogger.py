#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import gettext
import datetime
import platform

__author__ = "Muhammed Çamsarı"
__appname__ = "Opy-Logger"
__definition__ = "Used for simple log output."
__copyright__ = "Copyright (c) 2019 " + __author__
__license__ = "MIT"
__version__ = "2.0.1"
__status__ = "Beta"
__email__ = "muhammedcamsari@icloud.com"
__pgp__ = 'F294 1D36 A8C8 101B EEB0  16A7 B260 DBA5 2DAA 962A'

_ = gettext.gettext

def time():
	time = datetime.datetime.now()
	return time

class log:
	def __init__(self, registration=False, file=None, color=True, date=True):
		## registration: Logların kayıt etme durumunu belirtir.
		## file: Loglar kayıt ediliyorsa; kayıt dosyasını belirtir.
		## color: Logların renklendirme durumunu belirtir.
		## date: Loglardaki tarih durumunu belirtir.
		##

		self.kayit_durumu = registration
		self.kayit_dosyasi = file
		self.tarih_bilgisi = date

		## Renklendirme
		if color == True:
			self.Green = '\33[92m'
			self.Red = '\33[31m'
			self.Blue = '\33[34m'
			self.Yellow = '\33[33m'
			self.Pink = '\33[35m'
			self.BoldRed = '\033[1m' + '\33[31m'
			self.Grey = '\33[90m'
			self.NoColor = '\033[0m'
		elif color == False:
			self.Green = '\033[0m'
			self.Red = '\033[0m'
			self.Blue = '\033[0m'
			self.Yellow = '\033[0m'
			self.Pink = '\033[0m'
			self.BoldRed = '\033[0m'
			self.Grey = '\033[0m'
			self.NoColor = '\033[0m'

		# file değeri kontrol edilir
		if self.kayit_durumu == True:
			if self.kayit_dosyasi == None:
				print (_('[!] registration=True ama file= belirtilmemiş! Çıktılar dosyaya yazılmayacak.'))
			else:
				print (_('%s [%s] Çıktılar şuraya yazılacak: %s' % (time(), self.Blue + __appname__ + self.NoColor, self.kayit_dosyasi)))

	def writeline(file, inputs):
		color = ['[34m', '[0m', '[31m', '[33m', '[1m', '[35m', '[90m']

		file = open(file, 'a')
		for i in color:
			if i in inputs:
				inputs = inputs.replace(i, '')

		file.write(inputs + '\n')
		file.close()

	def appinfo(self, route='line', name=None, version=None, author=None, email=None, lisance=None, web=None):
		## 
		## route: Biçimlendirme şeklini belirtir.
		## name: Modülü kullanan uygulamanın adını belirtir.  
		## version: Modülü kullanan uygulamanın sürümünü belirtir.
		## author: Modülü kullanan uygulamanın geliştiricisinin adını belirtir.
		## email: Modülü kullanan uygulamanın geliştiricisinin E-Mail adresini belirtir.
		## lisance: Modülü kullanan uygulamanın lisans türünü belirtir.
		## web: Modülü kullanan uygulamanın geliştiricisinin Web adresini belirtir.
		##
		self.uygulama_bilgisi = ''
		print ('-' * 5, self.Green + _('Uygulama Bilgileri') + self.NoColor)

		# Satır/Boşluk Tercihi
		if route == 'line':
			route = '\n'

		elif route == 'tab':
			route = '\t'

		else:
			print (_('%s [%s] Hatalı yapılanma: %s. Varsayılan: line' % (time(), self.Blue + 'App Info' + self.NoColor, route)))
			route = '\n'

		# Uygulama Adı
		if name == None:
			pass
		else:
			name = _('Uygulama Adı: %s' % self.Blue + name + self.NoColor)
			self.uygulama_bilgisi += name + route

		# Uygulama Sürümü
		if version == None:
			pass
		else:
			version = _('Uygulama Sürümü: %s' % self.Blue + version + self.NoColor)
			self.uygulama_bilgisi += version + route

		# Geliştirici Adı
		if author == None:
			pass
		else:
			author = _('Uygulama Geliştiricisi: %s' % self.Blue + author + self.NoColor)
			self.uygulama_bilgisi += author + route

		# Geliştirici Mail Adresi
		if email == None:
			pass
		else:
			email = _('Uygulama Geliştiricisinin E-Mail Adresi: %s' % self.Blue + email + self.NoColor)
			self.uygulama_bilgisi += email + route

		# Lisans bilgisi
		if lisance == None:
			pass
		else:
			lisance = _('Uygulama Lisansı: %s' % self.Blue + lisance + self.NoColor)
			self.uygulama_bilgisi += lisance + route

		# Geliştirici Web Adresi
		if web == None:
			pass
		else:
			web = _('Uygulama Geliştiricisinin Web Adresi: %s' % self.Blue + web + self.NoColor)
			self.uygulama_bilgisi += web + route

		print (self.uygulama_bilgisi)

		if self.kayit_durumu == True:
			if not self.kayit_dosyasi == None:
				log.writeline(self.kayit_dosyasi, self.uygulama_bilgisi)


	def sysinfo(self):
		print ('-' * 5, self.Green + _('Sistem Bilgileri') + self.NoColor)
		self.sistem_bilgileri = ''

		modul_version = _('Opy-logger Sürümü: %s' % self.Blue + __version__ + self.NoColor) + '\n'
		sistem_ver = _('Çekirdek: %s' % self.Blue + platform.system() + self.NoColor) + '\n'
		makine = _('Makine: %s' % self.Blue + platform.machine() + self.NoColor) + '\n'
		python = _('Python Sürümü: %s' % self.Blue + platform.python_version() + self.NoColor) + '\n'
		derleyici = _('Derleyici: %s' % self.Blue + platform.python_compiler() + self.NoColor)

		self.sistem_bilgileri += modul_version + sistem_ver + makine + python + derleyici

		print (self.sistem_bilgileri)

		if self.kayit_durumu == True:
				if not self.kayit_dosyasi == None:
					log.writeline(self.kayit_dosyasi, self.sistem_bilgileri)


	def moduleinfo(self):
		print ('-' * 5, self.Green + _('%s Bilgileri') % __appname__ + self.NoColor)
		self.modul_bilgileri = ''

		surum = _('Sürüm: %s' % self.Blue + __version__ + self.NoColor) + '\n'
		yazar = _('Geliştirici: %s' % self.Blue + __author__ + self.NoColor) + '\n'
		lisans = _('Lisans: %s' % self.Blue + __license__ + self.NoColor) + '\n'
		destek = _('Destek: %s' % self.Blue + __email__ + self.NoColor) + '\n'
		Copyright = self.BoldRed + __copyright__ + self.NoColor

		self.modul_bilgileri += surum + yazar + lisans + destek + Copyright

		print (self.modul_bilgileri)


	def command(self, types, message, category, date):
		self.message = ''

		if types == 'info':
			types = self.Blue + _('[BILGI]') + ' ' + self.NoColor

		elif types == 'error':
			types = self.Red + _('[HATA]') + ' ' + self.NoColor

		elif types == 'warning':
			types = self.Yellow + _('[UYARI]') + ' ' + self.NoColor

		elif types == 'critical':
			types = self.BoldRed + _('[KRITIK]') + ' ' + self.NoColor

		elif types == 'output':
			types = self.Pink + _('[CIKTI]') + ' ' + self.NoColor

		elif types == 'debug':
			types = self.Grey + _('[HATA AYIKLAMA]') + ' ' + self.NoColor

		# Kategori 
		if category == None:
			category = ''
		else:
			category = '[' + category + '] '

		# Saat
		if self.tarih_bilgisi == False:
			date = ''

		elif date == True:
			date = str(time()) + ' '

		else:
			date = ''

		self.message = str(date) + str(types) + str(category) + str(message)

		print (self.message)

		if self.kayit_durumu == True:
			if not self.kayit_dosyasi == None:
				log.writeline(self.kayit_dosyasi, self.message)


	def info(self, message, category=None, date=True):
		log.command(self, 'info', message, category, date)

	def error(self, message, category=None, date=True):
		log.command(self, 'error', message, category, date)

	def warning(self, message, category=None, date=True):
		log.command(self, 'warning', message, category, date)

	def critical(self, message, category=None, date=True):
		log.command(self, 'critical', message, category, date)

	def output(self, message, category=None, date=True):
		log.command(self, 'output', message, category, date)

	def debug(self, message, category=None, date=True):
		log.command(self, 'debug', message, category, date)
