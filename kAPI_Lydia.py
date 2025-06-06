print("Demarrage 'API_lydia.py'")
from Requetes import *

#### Fonction de vérification d'une transaction lydia ####

def Lydia_check(token_public,montant,phone,order_id,Qrcode):

    #Convertit les données scannées du qrcode en un format comprehensible pour la requête Json
    paymentData = json.dumps(Qrcode)

    # Les données à envoyer à l'API
    data = {
        'vendor_token': token_public,
        'amount': montant,
        'phone': phone,
        'order_id': order_id,
        'paymentData': paymentData,
        'currency': 'EUR'
    }

    # Configuration optionnelle : désactiver la vérification SSL pour cet exemple.
    # En production, assurez-vous que SSL est activé et correctement configuré.
    requests.packages.urllib3.disable_warnings()

    # Effectuer la requête POST
    response = requests.post(config_lydia.url, data=data, verify=False)

    # Vérifier la réponse
    if response.status_code == 200:
        # Convertir la réponse en JSON
        response_data = response.json()
        
        try :
            if response_data['error'] == "0":
                Entrer_log(setting.projet_path, "Logs_prg","Transaction lydia réussie")
                Entrer_log(setting.projet_path, "Logs_prg", "Identifiant de la transaction :"+ str(response_data['transaction_identifier']))
                return response_data['transaction_identifier']
            else : 
                Entrer_log(setting.projet_path, "Logs_error","Code d'erreur survenu lors de la transaction :" + str(response_data['error']))
                return None
        except :
            Entrer_log(setting.projet_path, "Logs_error","L'erreur suivante est survenu lors de la transaction :" + str(response_data['status']) +"  :  " + str(response_data['message']))
            return None

    else:
        Entrer_log(setting.projet_path, "Logs_error","Erreur de requête HTTP :" + str(response.status_code))
        return None

