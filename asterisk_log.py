#!/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
#
#                     Module [asterisk_log] MLMConseil
#                    ----------------------------------
#
#                    ----------------------------------
#                   permet de recharger les appels d'asterisk
#                   par le fichier "Master.csv" 
#                  ----------------------------------------
#                       langage : Python 2.7
#                       date creation : 30/10/2015
#                       date modification : /2015
#                       version : 0.1
#                       auteur  : Bouslahi Yacine
#
################################################################################
from openerp.osv import fields, osv, orm
import logging
import datetime
import time
import sys, os
from config import *

_logger = logging.getLogger(__name__)

#PATH =
class asterisk_log(osv.Model):
    _name = 'asterisk.log'
    _description = "Informations sur les appels"
    _order = 'date' #'date desc'  DESC
    # _log_access = False

    _columns = {
        #'name': fields.many2one('res.partner', 'Nom'), 
        'appelant': fields.char('Appelant', size=50), #, required=True
        'appele': fields.char('Appelé', size=50),
        'date': fields.char('Date', size=50),
        'heure' : fields.char('Heure', size=50),
        'duree': fields.char('Durée', size=50),
        'etat': fields.char('Etat', size=50),
        #'total_appel': fields.function(_appel_total, string='total d\'appel', type='integer'),
    }

    def update_tree(self, cr, uid, ids, context=None):
        i = 0
        ligne_file = 0
        max_id = 0
        try:
            date_mnt = time.strftime("%d-%m-%Y")
            req1 = "SELECT max(id) FROM asterisk_log" #" SELECT COUNT(*) FROM asterisk_log"
            cr.execute(req1)
            id_appel = cr.fetchone()[0]
            if id_appel == None:
				id_appel = 0
            max_id = id_appel
            try:
                file = open(PATH,'r')
            except IOError:
                raise orm.except_orm(("Erreur :"),("fichier Master.csv introuvable %s" % (os.path.abspath(PATH))))
                # sys.exit(0)

            for ligne in file.readlines():
                if ligne_file > max_id-2: #changer a max_id-1
                    i +=1
                    appelant = str(ligne.split(",")[4].replace('"','')) # recupere au format Merouane <208>
                    appele = str(ligne.split(",")[2].replace('"',''))
                    #dans le cas ou c un appel entrant
                    if appele == '0033185092063':
                        appelant = str(ligne.split(",")[1].replace('"','')) # recuperer juste le num
                        date_heure = len(ligne.split(",")[13].replace('"','').split(" "))
                        if date_heure == 2:
                    		date = str(ligne.split(",")[13].replace('"','').split(" ")[0])
                    		heure = str(ligne.split(",")[13].replace('"','').split(" ")[1])
                    	else:
                    		date = str(ligne.split(",")[13].replace('"',''))
                    		heure = '00:00:00'
                    	duree = str(ligne.split(",")[15].replace('"',''))
                    	etat = str(ligne.split(",")[16].replace('"',''))
                     ##dans le cas ou c un appel sortant
                    else:
                        date_heure = len(ligne.split(",")[9].replace('"','').split(" "))
                        if date_heure == 2:
                			date = str(ligne.split(",")[9].replace('"','').split(" ")[0])
                			heure = str(ligne.split(",")[9].replace('"','').split(" ")[1])
                        else:
                			date = str(ligne.split(",")[9].replace('"',''))
                			heure = '00:00:00'
                        duree = str(ligne.split(",")[13].replace('"',''))
                        etat = str(ligne.split(",")[14].replace('"',''))
                	id_appel +=1
                	req = "INSERT INTO asterisk_log(id, etat, appele, create_date, create_uid, appelant, duree, write_uid, write_date, date, heure)        \
                        VALUES ({0}, '{5}', '{2}', '{6}', 1, '{1}', '{4}', 1,'{6}', '{3}', '{7}')".format(id_appel, appelant, appele, date, duree, etat, date_mnt, heure)

                    cr.execute(req)
                    cr.commit()
                    cr.close()
                ligne_file +=1

            file.close
            #print " Nombre de lignes inseree : %s" %i


        except Exception as err:
        	raise orm.except_orm(
				("Erreur :"),
                ("requete incorrecte %s" % err))
        	# sys.exit(0)

        else:
        	if i==0:
				raise orm.except_orm(("Mise à jour"),
					("Pas de nouvels appels"))
        	else:
				raise orm.except_orm(
					("Mise à jour reussie"),
            		("%s  Nouvels appels trouvés" % i))

        finally:
            _logger.info("Mise a jour des appels reussie: %s appels trouvé" % i)
