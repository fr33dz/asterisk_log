# -*- coding: utf-8 -*-

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
			up, i , msg= update_calls.update()
			if not up:
				raise orm.except_orm(
					("Erreur de mis à jour"),
                	("Details %s" % msg))
			elif up:
				raise orm.except_orm(
				("Mis à jour reussie"),
            	("la liste est mis a jour %s up = %s" % (i, up)))

		finally:
			 _logger.debug("Mise a jour des appels reussie: %s\%s appels trouvé" % (i, up))
			# raise orm.except_orm(
			# 	("saha"),
   #          	("la liste est mis a jour %s" % i))
        	    	

        # except Exception, e:
        #     raise orm.except_orm(
        #         _("Erreur de mis à jour"),
        #         _("Probleme d'nsertion de données %s" % e))
        # finally:
        #     if ast_manager:
        #         ast_manager.Logoff()
        # raise orm.except_orm(
        #     _("Mis à jour reussie"),
        #     _("la liste est mis a jour"))


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
