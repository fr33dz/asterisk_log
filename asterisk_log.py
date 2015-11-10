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
from openerp.osv import fields, osv, orm
import logging
import datetime
import update_calls

_logger = logging.getLogger(__name__)


#PATH = 
class asterisk_log(osv.Model):
	_name = 'asterisk.log'
	_description = "Informations sur les appels"
	_order = 'date' #'date desc'  DESC 
	# _log_access = False

	def update_tree(self, cr, uid, ids, context=None):
		i = 0
		up = None
		try:
			#Appel de la fonction update du fichier update_calls.py
			#masquer la variable up 
			up, i , msg= update_calls.update() 
			if not up:
				raise orm.except_orm(
					("Erreur de mise à jour"),
                	("Details %s" % msg))
			elif up:
				if i==0:
					raise orm.except_orm(("Mise à jour"),
						("Pas de nouvels appels"))
				else:
					raise orm.except_orm(
					("Mise à jour reussie"),
            		("%s  Nouvels appels trouvés" % i))

		finally:
			 _logger.info("Mise a jour des appels reussie: %s\%s appels trouvé" % (i, up))


	_columns = {
		#'name': fields.many2one('res.partner', 'Nom'),
		'appelant': fields.char('Appelant', size=50), #, required=True
		'appele': fields.char('Appelé', size=50),
		'date': fields.char('Date', size=50),
		'heure' : fields.char('Heure', size=50),
		'duree': fields.char('Durée', size=50),
		'etat': fields.char('Etat', size=50),
		#'mise_a_jour': fields.char('Etat', size=50, required=True),
	}
