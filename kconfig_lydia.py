print("Demarrage 'config_lydia.py'")


#### Fichier de définitions des TOKENS et numéro de téléphone utilisé pour les transactions ####
# Décommentez l'url adéquat selon l'utilisation de la borne #
# Décommentez le token adéquat selon l'utilisation de la borne #
# Le numéro de phone utilisé doit être le numéro d'un caissier du compte lydia d'encaissement #

class config_lydia :
    # L'URL de l'API pour initier une transaction (remplacer par l'URL de test ou de production selon le cas)
    #url = "https://lydia-app.com/api/payment/payment.json"   # Production
    url = "https://homologation.lydia-app.com/api/payment/payment.json"    # Test

    # TOKENS DE TEST pour le site Kfet
    #token_public = "58ada276ab575970477137" #pour les appels
    #token_prive = "58ada276ad930951358751" #pour la signature

    # TOKENS DE PRODUCTION pour le site Kfet
    token_public = "56b21e42103d7715736202" #pour les appels
    token_prive = "56b21e4212e2b468320228" #pour la signature

    # TOKENS DE TEST pour l'activité du Bapt'ss
    # token_public = "67476a1346f62188940343" #pour les appels
    # token_prive = "67476a134f166561760862" #pour la signature

    # TOKENS DE PRODUCTION pour l'activité du Bapt'ss
    #token_public = "5b19630a40892684681512" #pour les appels
    #token_prive = "5b19630a5101a987821327" #pour la signature

    # TOKENS DE TEST pour l'activité des 100J
    #token_public = "660e5b8b4c353994613407" #pour les appels
    #token_prive = "660e5b8b52b31218065719" #pour la signature

    # TOKENS DE PRODUCTION pour l'activité des 100J
    #token_public = "54c10dbc666a3894276098" #pour les appels
    #token_prive = "54c10dbc67804505863299" #pour la signature

    # Numéro de téléphone du caissier pour la cagnote des 100J
    #phone='33782977418' # Phone d'un gripss O 223
    #phone = '33632994795'  # Phone d'un gripss O 222
    phone='0656683464' # Phone de test en environnement d'homologation pour le bapt'sss

