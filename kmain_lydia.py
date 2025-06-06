print("Demarrage 'main_lydia.py'")
from API_lydia import *

#### Programme principale de la transaction lydia avec MAJ BDD ####
def Recharge_montant(UID,montant):
    Money=SQL_SELECT(QUERRY_getMoney(UID))[0][0]
    SQL_EXECUTE(QUERRY_setMoney(UID,Money+montant))


def Transaction_Lydia(box, UID, montant, Qrcode, token_public, phone):

    # 1) Récupération de la date courrante et insertion de l'id de la transaction a effectuée avec l'UID de la carte
    current_date = SQL_SELECT(QUERRY_getTime())[0][0]
    SQL_EXECUTE(QUERRY_setIdLydia(UID,montant,current_date))

    # 2) Récupération de l'id de cette transaction
    order_id = SQL_SELECT(QUERRY_getIdLydia(current_date))[0][0]

    # 3) Vérification de la transaction avec l'API lydia
    transaction_identifier = Lydia_check(token_public, montant, phone, order_id, Qrcode)

    # 4) Si paiement validé (check != None): MAJ montant de la carte BDD et table lydia
    if transaction_identifier:
        montant = montant  # en centime pour la bdd
        Recharge_montant(UID, montant)
        SQL_EXECUTE(set_Transaction_Lydia(order_id,transaction_identifier))
        SQL_EXECUTE(QUERRY_setCredit_update(UID,montant,current_date))
        Entrer_log(setting.projet_path, "Logs_prg", "Mise à jour de la BDD effectuée avec succès")
       return True

   # 5) Si paiement refusé
   else:
       Entrer_log(setting.projet_path, "Logs_error", "Problème survenu lors de la transaction")
       return False
