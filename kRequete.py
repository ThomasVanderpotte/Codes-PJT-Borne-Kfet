print("Démarrage 'Requete.py'")
def QUERRY_getMoney(users_id):
    return(("SELECT credit FROM users WHERE users.id='{}';").format(users_id))
old_credit=SQL_SELECT(QUERRY_getMoney(idusers))[0][0]
def QUERRY_setMoney(idusers,Money):
    
    return(("UPDATE users SET credit='{}' WHERE users.id='{}'; ").format(Money,idusers))
    
def add_RFID(UID, id_RFID):
    return (("UPDATE users SET RFID = '{}' WHERE id = '{}';").format(id_RFID, UID))

def QUERRY_getTime():
    return (("SELECT NOW();"))

def QUERRY_setIdLydia(idusers,montant,date):
    
    return(("INSERT INTO consos_lydia (users_id, montant, date) VALUES ('{}', '{}', '{}', '{}');").format(user_id, montant, UNIX_TIMESTAMP(date)) )  

def QUERRY_getIdLydia(date):
    return(("SELECT id FROM consos_lydia WHERE date= '{}';").format(date))#verifier si c'est le bon id

def QUERRY_setCredit_update(idusers,Money,date):
    return(("INSERT INTO log_credit_update (id_user, montant_avant, montant_apres,date) VALUES ('{}', '{}', '{}') ").format(idusers,old_credit,Money+old_credit,date))
    
def set_Transaction_Lydia(order_id,transaction_identifier):
    return(("UPDATE consos_lydia SET transaction_identifier)='{}' WHERE id='{}';").format(transaction_identifier,order_id))
    
        
        

        

