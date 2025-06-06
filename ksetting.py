print("Demarrage 'setting.py'")
from importation import *

# Définition des variables reliée à l'objet setting définissant les paramètres de la box. Ces paramètres sont sauvegardés et résistent au reboot
class setting:
    projet_path = "/".join(__file__.split("/")[:-2]) + "/"
    # Nom de la box (Données par la BDD au démarrage), il définie le rôle de la box selon la première lettre (ATTENTION: Première lettre toujours en majuscule)
    nomBox='Automatique'#A pour BorneAutomatique de toute manière le code ne prend que la 1er lettre du nom
    # Numéro de la box, permet d'identifié de façon unique les boxs (clé primaire) pour la BDD
    numeroBox=91
    # Version du système, permet de savoir quand une MAJ est a faire
    version='610'
    # Paramètre indiquand au système si la box a ping le serveur (010)
    rezalOn=False
    # Paramètre indiquand si la box est en mode hors ligne ou pas (001)
    rezalMode=True
    # Paramètre indiquant si la box à ping un réseau internet(100)
    rezalNet=False
    # IP de la box
    IP='192.168.1.91'
    # Adresse MAC de la box
    MAC='02:07:84:40:6b:94'
    # Dictionnaire des produits de la box
    produits={}
    # Définition du dictionnaire de connection à la BDD
    # Nom d'utilisateur
    # Mot de passe du nom d'utilisateur
    # Nom de la BDD
    # IP du serveur BDD
    connection = {"user": 'pi',
                  "password": 'pi',
                  "database": 'GestionKIN',
                  "host": '192.168.1.100'}
    serveurNet = "8.8.8.8"
# Adresse IP DNS google qui répond au ping



        
        
    
        
        

        

