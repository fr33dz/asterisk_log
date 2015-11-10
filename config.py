#!/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
#
#                     Module [asterisk_log] MLMConseil
#                    ----------------------------------
#
#                    ----------------------------------
#                   permet de connecter à PostgreSQL et inserer
#                   les nouvels appels d'asterisk
#                  ----------------------------------------
#                       langage : Python 2.7
#                       date creation : 30/10/2015
#                       date modification : /2015
#                       version : 0.1
#                       auteur  : Bouslahi Yacine
#
################################################################################



########################## POSTGRESQL CONFIG

HOST = '127.0.0.1' 
PORT = 5432          
DATABASE = 'BDD_Translation'
USER = 'openpg'     
PASSWORD = 'openpgpwd'		

########################## Master.csv Path 
PATH = 'C:\\Program Files (x86)\\Odoo 8.0-20150719\\server\\openerp\\addons\\asterisk_log\\Master.csv'#'Master.csv'   # chemin vers le fichier Master.csv
