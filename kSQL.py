print("Demarrage 'SQL.py'")
from config_lydia import *

#### Définition des fonctions d'exécution des requêtes ####

def SQL_SELECT(querry):
    _cnx=mysql.connector.connect(**setting.connection)
    _cursor=_cnx.cursor()
    _cursor.execute(querry)
    _select=_cursor.fetchall()
    _cnx.close()
    return _select

def SQL_EXECUTE(querry):
    _cnx=mysql.connector.connect(**setting.connection)
    _cursor=_cnx.cursor()
    _cursor.execute(querry)
    _cnx.commit()
    _cnx.close()
    ##DATA_add(setting.projet_path+'PICONFLEX2000-LOGS/LOG_SQL.txt',querry+"\n")
