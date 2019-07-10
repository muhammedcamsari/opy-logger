#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import platform

__author__ = "Muhammed Çamsarı"
__appname__ = "OPY-Logger"
__definition__ = "Used for simple log output."
__copyright__ = "Copyright (c) 2019 " + __author__
__license__ = "MIT"
__version__ = "1.0"
__status__ = "Beta"
__email__ = "muhammedcamsari@icloud.com"
__pgp__ = 'F294 1D36 A8C8 101B EEB0  16A7 B260 DBA5 2DAA 962A'

Green = '\33[92m'
Red = '\33[31m'
Blue = '\33[34m'
Yellow = '\33[33m'
BoldRed = '\033[1m' + '\33[31m'
Grey = '\33[90m'
NoColor = '\033[0m'
 
def init(name=None, version=None, author=None, url=None):
	print ('-' * 3 , Green + 'App Info' + NoColor, '-' * 23)
	if not name == None:
		name = 'Name: ' + Blue + name + NoColor
	else:
		name = ''

	if not version == None:
		version = 'Version: ' + Blue + version + NoColor
	else:
		version = ''

	if not author == None:
		author = 'Author: ' + Blue + author + NoColor
	else:
		author = ''

	if not url == None:
		url = 'Website: ' + Blue + url + NoColor
	else:
		url = ''

	print (name, version, author, url)

def sysinfo():
	print ('-' * 3 , Green + 'System Info' + NoColor, '-' * 20)
	print (__appname__ + ' Version: ' + Blue + __version__ + NoColor)
	print ('System: ' + Blue + platform.system() + NoColor)
	print ('Machine: ' + Blue + platform.machine() + NoColor)
	print ('Python: ' + Blue + platform.python_version() + NoColor)
	print ('Compiler: ' + Blue + platform.python_compiler() + NoColor)

def moduleinfo():
	print ('-' * 3 , Green + 'Module Info' + NoColor, '-' * 20)
	print ('Name: ' + Blue + __appname__ + NoColor)
	print ('Version: ' + Blue + __version__ + __status__ + NoColor)
	print ('Author: ' + Blue + __author__ + NoColor)
	print ('License: ' + Blue + __license__ + ' License' + NoColor)
	print ('Support: ' + Blue + __email__ + NoColor)
	print (Blue + __copyright__ + NoColor)


def debug(message, category=None, date=True):
	if category == None: # Kategori yoksa
		if date == True: # Tarih Aktifse
			print (datetime.datetime.now(), Grey + '[DEBUG]' + NoColor, message)

		elif date == False: # Tarih aktif değilse
			print (Grey + '[DEBUG]' + NoColor, message)

	else: # Kategori varsa
		if date == True: # Tarih Aktifse
			print (datetime.datetime.now(), Grey + '[DEBUG]' + NoColor, '[%s]' % category, message)

		elif date == False: # Tarih aktif değilse
			print (Grey + '[DEBUG]' + NoColor, '[%s]' % category, message)

def info(message, category=None, date=True):
	if category == None: # Kategori yoksa
		if date == True: # Tarih Aktifse
			print (datetime.datetime.now(), Blue + '[INFO]' + NoColor, message)

		elif date == False: # Tarih aktif değilse
			print (Blue + '[INFO]' + NoColor, message)

	else: # Kategori varsa
		if date == True: # Tarih Aktifse
			print (datetime.datetime.now(), Blue + '[INFO]' + NoColor, '[%s]' % category, message)

		elif date == False: # Tarih aktif değilse
			print (Blue + '[INFO]' + NoColor, '[%s]' % category, message)

def warning(message, category=None, date=True):
	if category == None: # Kategori yoksa
		if date == True: # Tarih Aktifse
			print (datetime.datetime.now(), Yellow + '[WARNING]' + NoColor, message)

		elif date == False: # Tarih aktif değilse
			print (Yellow + '[WARNING]' + NoColor, message)

	else: # Kategori varsa
		if date == True: # Tarih Aktifse
			print (datetime.datetime.now(), Yellow + '[WARNING]' + NoColor, '[%s]' % category, message)

		elif date == False: # Tarih aktif değilse
			print (Yellow + '[WARNING]' + NoColor, '[%s]' % category, message)

def error(message, category=None, date=True):
	if category == None: # Kategori yoksa
		if date == True: # Tarih Aktifse
			print (datetime.datetime.now(), Red + '[ERROR]' + NoColor, message)

		elif date == False: # Tarih aktif değilse
			print (Red + '[ERROR]' + NoColor, message)

	else: # Kategori varsa
		if date == True: # Tarih Aktifse
			print (datetime.datetime.now(), Red + '[ERROR]' + NoColor, '[%s]' % category,  message)

		elif date == False: # Tarih aktif değilse
			print (Red + '[ERROR]' + NoColor, '[%s]' % category, message)

def critical(message, category=None, date=True):
	if category == None: # Kategori yoksa
		if date == True: # Tarih Aktifse
			print (datetime.datetime.now(), BoldRed + '[CRITICAL]' + NoColor, message)

		elif date == False: # Tarih aktif değilse
			print (BoldRed + '[CRITICAL]' + NoColor, message)

	else: # Kategori varsa
		if date == True: # Tarih Aktifse
			print (datetime.datetime.now(), BoldRed + '[CRITICAL]' + NoColor, '[%s]' % category, message)

		elif date == False: # Tarih aktif değilse
			print (BoldRed + '[CRITICAL]' + NoColor, '[%s]' % category, message)