print("Démarrage 'boot.py'")

from Main_affichage import *

Entrer_log(setting.projet_path, "Logs_prg", "Démarage Programe")


root=MainApp()
root.mainloop()

if config.debugging :
    print("Attente de 3s")
    sleep(3)

