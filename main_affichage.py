print("Demarrage 'main_affichage.py'")

from Template_pageV2 import *


class MainApp(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.top = Page(self)
        self.withdraw()
        self.mode = "Carte"
        self.sleeping_mode = True
        self.L_presence_card = []
        self.Boucle()




    def Boucle(self):
        if self.sleeping_mode:
            if self.Verif_Rezal():
                self.sleeping_mode = False

                Entrer_log(setting.projet_path, "Logs_prg", "MODE : "+ str(self.mode))
                print("MODE : " + self.mode)

                
                elif self.mode == "Montant":
                    self.Montants()
                elif self.mode == "QR":
                    self.QR()
                elif self.mode == "Transaction":
                    self.QR_checkUID()
                elif self.mode == "Error_QR":
                    self.Error_QR()
                
                elif self.mode == "Error_Montant":
                    self.Error_montant()
                elif self.mode == "Error_Rezal":
                    self.Error_rezal()
                elif self.mode == "Error_Matos":
                    self.Error_matos()
                elif self.mode == "Finish":
                    self.Finish()
               
                else:
                    print("wrong mode ducon")
            else :
                print("error plus de coo")
                Entrer_log(setting.projet_path, "Logs_co", "Connection perdue")
                self.Error_rezal()


        if self.mode in ["Montant", "QR", "Transaction","Finish"]:
            self.Carte_test()

        self.after(100, self.Boucle)

    def Verif_Rezal(self):
        Entrer_log(setting.projet_path,"Logs_co" , "Test des connections")

        self.Test_Rezal()
        if (setting.rezalOn and setting.rezalNet):
            Entrer_log(setting.projet_path, "Logs_co", "Connections établies avec succès")
            return True
        else:
            Entrer_log(setting.projet_path, "Logs_co", "Connections non établies")
            return False

    def Test_Rezal(self):  # Fonction de vérification du réseau
        try:
            if REZAL_pingServeur():  # Ping du serveur guinche pour s'assurer que la connection locale est toujours présente
                Entrer_log(setting.projet_path, "Logs_co", "Connection à la BDD OK")
                DATA_setVariable("rezalOn", bool(REZAL_pingServeur()))
                if REZAL_pingInternet():  # Ping du serveur google pour s'assurer que la connection internet est toujours présente
                    Entrer_log(setting.projet_path, "Logs_co", "Connection à internet OK")
                    DATA_setVariable("rezalNet", bool(REZAL_pingInternet()))
                    return None
                else:
                    Entrer_log(setting.projet_path, "Logs_co", "La connection au serveur google a échoué")
                    DATA_setVariable("rezalNet", bool(False))
                    return None
            else:
                Entrer_log(setting.projet_path, "Logs_co", "La connection au serveur Guinche a échoué")
                DATA_setVariable("rezalOn", bool(False))
                return None
            
     

    def Montants(self):
        if command_usb('keyboard','enable') and command_usb('scan','disable'):
            self.top.Page_montant(self.argent)
        else:
            self.mode = "Error_Matos"
            Entrer_log(setting.projet_path, "Logs_error", "Probleme avec le matériel")
            self.sleeping_mode = True


    def Check_montants(self, montant):
        self.montant = int(montant)
        Entrer_log(setting.projet_path, "Logs_prg", "Montant de la recharge souhaitée : " + str(self.montant))
        if self.montant > config.maxTransaction / 100 or (
                self.montant + self.argent) > config.maxMontant / 100 or self.montant == 0:  # Vérifie le montant de la recharge
            self.mode = "Error_Montant"
            Entrer_log(setting.projet_path, "Logs_error", "Montant incorrecte")
        else:
            self.mode = "QR"
        self.sleeping_mode = True

    def QR(self):
        if command_usb('keyboard','disable') and command_usb('scan','enable'):
            self.top.Page_QR()
        else:
            self.mode = "Error_Matos"
            Entrer_log(setting.projet_path, "Logs_error", "Probleme avec le matériel")
            self.sleeping_mode = True

    def QR_check(self, QR):
        try:
            self.QRcode = eval(QR)
            Entrer_log(setting.projet_path, "Logs_prg", "QR code scanné")
            self.mode = "Transaction"
        except:
            self.mode = "Error_QR"
            Entrer_log(setting.projet_path, "Logs_error", "Probleme avec le Qr code")
        self.sleeping_mode = True

    


    def QR_transact(self, uid=None):
    Entrer_log(setting.projet_path, "Logs_prg", "Début de la transaction sans vérification d'UID")

    Entrer_log(setting.projet_path, "Logs_prg", "Identifiant du QR code : " + str(self.QRcode))

    if Transaction_Lydia(setting.numeroBox, self.UID, self.montant, self.QRcode, config_lydia.token_public, config_lydia.phone):
        Entrer_log(setting.projet_path, "Logs_prg", "Transaction Lydia effectuée avec succès")

        # Suppression de l’écriture RFID
        # RFID_setArgent(...) supprimé

        self.mode = "Finish"
    else:
        self.mode = "Error_QR"
        Entrer_log(setting.projet_path, "Logs_error", "Erreur lors de la transaction Lydia")

    self.sleeping_mode = True



    def Error_QR(self):
        self.top.Page_error_QR()
        self.after(5000, self.rollback, self.mode)

    def Error_carte(self):
        self.top.Page_error_carte()
        self.after(5000, self.rollback, self.mode)

    def Error_montant(self):
        self.top.Page_error_montant()
        self.after(5000, self.rollback, self.mode)

    def Error_rezal(self):
        self.top.Page_error_rezal()
        self.after(5000, self.rollback, self.mode)

    def Error_matos(self):
        self.top.Page_error_matos()
        self.after(5000, self.rollback, self.mode)

    def Finish(self):
        self.top.Page_confirmation()

    

    def rollback(self, mode):
        if mode==self.mode:
            self.mode = "Carte"
            self.sleeping_mode = True