#!/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
#
#                     Module [update_calls] MLMConseil
#                    ----------------------------------
#
#                    ----------------------------------
#                   permet de connecter à PostgreSQL et inserer
#                   les nouvels appels
#                  ----------------------------------------
#                       langage : Python 2.7
#                       date creation : 30/10/2015
#                       date modification : /2015
#                       version : 0.1
#                       auteur  : Bouslahi Yacine
#
################################################################################
import time
import psycopg2
import sys, os
import logging
from config import *


# _logger = logging.getLogger(__name__)
#from pprint import pprint

#import ipdb; ipdb.set_trace()

def update():
    con = None
    i = 0
    ligne_file = 0
    max_id = 0
    try:
        con = psycopg2.connect(host=HOST, port=PORT ,database=DATABASE, user=USER, password=PASSWORD)
        cur = con.cursor()
        try:
            date_mnt = time.strftime("%d-%m-%Y")
            req1 = "SELECT max(id) FROM asterisk_log" #" SELECT COUNT(*) FROM asterisk_log"
            cur.execute(req1)
            #print date_mnt
            cur.execute(req1)
            id_appel = cur.fetchone()[0]
            if id_appel == None:
                id_appel = 0

            max_id = id_appel
            try:
                file = open(PATH,'r')

            except IOError:
                print "Erreur : fichier Master.csv introuvable %s" % (os.path.abspath(PATH))
                # _logger.info("Erreur : fichier Master.csv introuvable %s" % (os.path.abspath(PATH)))
                return False, i, "Erreur : fichier Master.csv introuvable %s" % (os.path.abspath(PATH))
                sys.exit(0)
            
            for ligne in file.readlines():

##                print "Appelant : "+str(ligne.split(",")[1].replace('"','')) \
##                +"\t Appele : "+str(ligne.split(",")[2].replace('"','')) \
##                +"\t Date-heure : "+str(ligne.split(",")[9].replace('"','')) \
##                +"\t Duree : "+str(ligne.split(",")[13].replace('"','')) \
##                +"\t Etat : "+str(ligne.split(",")[14].replace('"',''))
                
                if ligne_file > max_id-2: #changer a max_id-1
                    i +=1
                    appelant = str(ligne.split(",")[4].replace('"','')) #str(ligne.split(",")[1].replace('"','')) retourne le num
                    appele = str(ligne.split(",")[2].replace('"','')) #dans le cas ou c un appel entrant
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

                    cur.execute(req)
                ligne_file +=1

            file.close
            print " Nombre de lignes inseree : %s" %i


        except Exception as err:
            print "Erreur lors de l'execution de la requete : %s" %err
            #heure = 0
            print "date  : %s , heure : %s" % (date, heure)

            return False, i, "Erreur lors de l'execution de la requete : %s" %err
            sys.exit(1)

    except psycopg2.DatabaseError, e:
        print 'Error %s' % e
        return False, i, "Erreur de base de données : %s" %err
        sys.exit(1)

    else:
        if con:
            con.commit()
            con.close()
            return True, i, "Insertion reussie"

    # finally:
    #     if con:
    #         con.commit()
    #         con.close()
    #     return True, i

# def main():
#     update()

# if __name__ == '__main__':
#     main()
