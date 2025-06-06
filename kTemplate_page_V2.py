

print("Demarrage 'Template_pageV2.py'")
from Config_Affichage import *




    def Page_montant(self,inmo):
        self.cancel_canvas()
        self.dico={"&":1, "é":2, '"':3, "'":4, "(":5, "-":6, "è":7, "_":8, "ç":9, "à":0}

      
    def Page_QR(self):
        self.cancel_canvas()

       


    def Page_error_QR(self):
        self.cancel_canvas()
        self.canvas.itemconfig(self.titre, text=txt_titre["error_QR"])
        self.canvas.itemconfig(self.top, state='normal', text=txt_indic["error_QR"])
        self.canvas.itemconfig(self.img, state="normal", image=self.imgtk['exclam'])

    def Page_error_montant(self):
        self.cancel_canvas()
        self.canvas.itemconfig(self.titre, text=txt_titre["error_montant"])
        self.canvas.itemconfig(self.top, state="normal", text=txt_indic["error_montant"])
        self.canvas.itemconfig(self.img, state="normal", image=self.imgtk['exclam'])

    
    def Page_error_rezal(self):
        self.cancel_canvas()
        self.canvas.itemconfig(self.titre, text=txt_titre["error_rezal"])
        self.canvas.itemconfig(self.top, state="normal", text=txt_indic["error_rezal"])
        self.canvas.itemconfig(self.img, state="normal", image=self.imgtk['exclam'])

   