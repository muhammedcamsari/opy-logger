#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## Opy-logger test.py

import opylogger

log = opylogger.log(registration=True, file='log.log')

log.sysinfo()

log.moduleinfo()

log.appinfo('line', name='test.py', version='1.2.3', author='Mr. X', lisance='BSD', email='example@example.com', web='https://Github.com')

log.error("HATA", 'GLIB')
log.error("HATA")
log.error("HATA", date=False)

log.warning("UYARI", 'THREAD')
log.warning("UYARI")
log.warning("UYARI", date=False)

log.debug("HATA AYIKLAMA", 'PyGobject')
log.debug("HATA AYIKLAMA")
log.debug("HATA AYIKLAMA", date=False)

log.critical("KRITIK", 'TKINTER')
log.critical("KRITIK")
log.critical("KRITIK", date=False)

log.info("BILGI", 'Numpy')
log.info("BILGI", )
log.info("BILGI", date=False)

log.output("ÇIKTI", 'CODE')
log.output("ÇIKTI")

log.output("ÇIKTI", date=False)