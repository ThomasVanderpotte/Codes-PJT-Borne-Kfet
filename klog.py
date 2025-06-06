print("Demarrage 'LOG.py'")
from config import *

def LOG_add(fichierName,contenu):
    _tmp=open(fichierName,"a")
    _tmp.write(str(contenu))
    _tmp.close()


def Entrer_log (projet_path,nom_fichier_log,contenu):   # Toutes les variables en str
    os.makedirs(nom_fichier_log, exist_ok=True)
    now=ctime()
    LOG_add(projet_path+'/'+nom_fichier_log,"At: "+str(now)+":"+contenu+"\n")


####Exemple d'entrée de log.txt
#Entrer_log(os.path.abspath(os.path.dirname(__file__)),'LOG.txt','self.mode=='+'carte'+' heure: '+str(datetime.datetime.now())+"\n")
####

