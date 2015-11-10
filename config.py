#!/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
#
#                     Module [] MLMConseil
#                    ----------------------------------
#
#                    ----------------------------------
#                   Ce fichier sert a configurer le module
#                  ----------------------------------------
#                       langage : Python 2.7
#                       date creation : /2015
#                       date modification : /2015
#                       version : 0.1
#                       auteur  : Bouslahi Yacine
#
###############################################################################



########################## POSTGRESQL CONFIG

HOST = '127.0.0.1' #'192.168.1.10'
PORT = 5432          #5433
DATABASE = 'BDD_Translation'
USER = 'openpg'     #'php'
PASSWORD = 'openpgpwd'		#'php'

########################## CLIENT CONFIG
PATH = 'C:\\Program Files (x86)\\Odoo 8.0-20150719\\server\\openerp\\addons\\asterisk_log\\Master.csv'#'Master.csv'   # chemin vers le fichier Master.csv
TIMER = 120 # temps d'actualisation