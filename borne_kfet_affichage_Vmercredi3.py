import sqlite3
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image

# Connexion à la base SQLite
conn = sqlite3.connect("kfet.db")
cursor = conn.cursor()

# Fenêtre principale
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
app = ctk.CTk()
app.title("Borne Kfet")
app.geometry("600x700")

# Configuration du focus
app.after(100, lambda: champ_fams.focus_set() if champ_fams.winfo_ismapped() else None)

# Charger et afficher le logo
try:
    image = Image.open("logokfetpaint.png")
    logo = ctk.CTkImage(light_image=image, dark_image=image, size=(200, 100))
    logo_label = ctk.CTkLabel(app, image=logo, text="")
    logo_label.pack(pady=10)
except:
    logo_label = ctk.CTkLabel(app, text="Logo Kfet", font=("Arial", 24))
    logo_label.pack(pady=10)

# Texte d'accueil
label_titre = ctk.CTkLabel(app, text="Borne Kfet", font=("Arial", 24, "bold"))
label_titre.pack(pady=5)

# Label "Compte de quel PG" (sera affiché/masqué dynamiquement)
label_question = ctk.CTkLabel(app, text="Compte de quel PG ?", font=("Arial", 18))
label_question.pack(pady=5)

# Variables globales
compte_actuel = None
suggestions = []
selection_mode = False

# Champ de recherche (sera affiché/masqué dynamiquement)
champ_fams = ctk.CTkEntry(app, font=("Arial", 16), width=300)
champ_fams.pack(pady=10)
champ_fams.focus_set()

# Zone d'affichage des suggestions
frame_suggestions = ctk.CTkFrame(app)
frame_suggestions.pack(pady=5)
labels_suggestions = []

# Indicateur de mode sélection
selection_indicator = ctk.CTkLabel(app, text="", font=("Arial", 12))
selection_indicator.pack()

# Instructions
label_instr1 = ctk.CTkLabel(app, text="- Appuyez sur entrée pour sélectionner un compte", font=("Arial", 12))
label_instr2 = ctk.CTkLabel(app, text="- Appuyez sur entrée puis 0 pour effacer la fams et recommencer", font=("Arial", 12))
label_instr1.pack()
label_instr2.pack()

# Informations du compte
infos = ctk.CTkLabel(app, text="", font=("Arial", 14), justify="left")
infos.pack(pady=10)

# Boutons d'action
frame_actions = ctk.CTkFrame(app)
buttons = [
    ctk.CTkButton(frame_actions, text="1 - Recharger", command=lambda: executer_action(1)),
    ctk.CTkButton(frame_actions, text="2 - Associer carte kgibs", command=lambda: executer_action(2)),
    ctk.CTkButton(frame_actions, text="3 - Passer à un autre compte", command=lambda: executer_action(3)),
    ctk.CTkButton(frame_actions, text="4 - Switcher mode clair/sombre", command=lambda: executer_action(4))
]
for btn in buttons:
    btn.pack(pady=2)

def toggle_champ_fams(visible):
    if visible:
        champ_fams.pack(pady=10)
        champ_fams.focus_set()
    else:
        champ_fams.pack_forget()

def chercher_fams(partiel):
    cursor.execute("SELECT * FROM comptes WHERE Fams LIKE ?", (f'%{partiel}%',))
    return [dict(zip([col[0] for col in cursor.description], row)) for row in cursor.fetchall()]

def afficher_suggestions():
    global labels_suggestions
    
    # Nettoyer les anciennes suggestions
    for label in labels_suggestions:
        label.destroy()
    labels_suggestions = []
    
    # Afficher les nouvelles suggestions (une sous l'autre)
    for i, compte in enumerate(suggestions[:10]):
        frame_compte = ctk.CTkFrame(frame_suggestions)
        frame_compte.pack(fill="x", pady=2)
        
        # Indicateur de sélection (flèche ou numéro)
        if selection_mode:
            indicateur = ctk.CTkLabel(frame_compte, text=f"→ {i+1}.", width=30, font=("Arial", 14))
            indicateur.pack(side="left")
        else:
            indicateur = ctk.CTkLabel(frame_compte, text=f"{i+1}.", width=30, font=("Arial", 14))
            indicateur.pack(side="left")
        
        # Info du compte
        label = ctk.CTkLabel(frame_compte, 
                            text=f"{compte['Fams']} ({compte['BdP']})", 
                            font=("Arial", 14),
                            anchor="w")
        label.pack(side="left", fill="x", expand=True)
        
        labels_suggestions.append(frame_compte)
    
    # Mise à jour de l'indicateur de mode
    if selection_mode:
        selection_indicator.configure(text="▼ Sélectionnez un compte avec son numéro ▼", text_color="#4cc9f0")
        toggle_champ_fams(False)  # Masquer la barre de texte
    else:
        selection_indicator.configure(text="")
        if not compte_actuel:  # Ne pas afficher si compte déjà sélectionné
            toggle_champ_fams(True)

def afficher_infos(compte):
    global compte_actuel
    compte_actuel = compte
    infos.configure(text=(
        f"BdP: {compte['BdP']}\n"
        f"Bucque: {compte['Bucque']}\n"
        f"Fams: {compte['Fams']}\n"
        f"Brosoufs: {compte['Brosoufs']}\n"
        f"Carte kgibs: {compte.get('Carte_kgibs', '')}\n\n"
        "Actions rapides :\n"
        "1-Recharger  2-Associer carte\n"
        "3-Changer compte  4-Changer thème"
    ))
    frame_actions.pack(pady=10)
    toggle_champ_fams(False)  # Masquer la barre de texte
    label_question.pack_forget()
    selection_indicator.configure(text="")

def executer_action(code):
    global compte_actuel, suggestions
    
    if code == 1:  # Recharger
        if not compte_actuel:
            return
            
        dialog = ctk.CTkInputDialog(text="Montant à ajouter:", title="Rechargement")
        dialog.after(100, lambda: dialog._entry.focus_set())
        montant = dialog.get_input()
        
        if montant and montant.isdigit():
            nouveau_montant = compte_actuel['Brosoufs'] + int(montant)
            cursor.execute("UPDATE comptes SET Brosoufs=? WHERE id=?", (nouveau_montant, compte_actuel['id']))
            conn.commit()
            compte_actuel['Brosoufs'] = nouveau_montant
            afficher_infos(compte_actuel)
            messagebox.showinfo("Succès", f"{montant} brosoufs ajoutés!")
    
    elif code == 2:  # Associer carte
        if not compte_actuel:
            return
            
        dialog = ctk.CTkInputDialog(text="ID de la carte kgibs:", title="Association carte")
        dialog.after(100, lambda: dialog._entry.focus_set())
        carte = dialog.get_input()
        
        if carte:
            cursor.execute("UPDATE comptes SET Carte_kgibs=? WHERE id=?", (carte, compte_actuel['id']))
            conn.commit()
            compte_actuel['Carte_kgibs'] = carte
            afficher_infos(compte_actuel)
            messagebox.showinfo("Succès", "Carte associée avec succès!")
    
    elif code == 3:  # Changer compte
        reset_recherche()
    
    elif code == 4:  # Changer thème
        current_mode = ctk.get_appearance_mode()
        new_mode = "light" if current_mode == "dark" else "dark"
        ctk.set_appearance_mode(new_mode)
        if compte_actuel:
            afficher_infos(compte_actuel)

def reset_recherche():
    global compte_actuel, suggestions, selection_mode
    compte_actuel = None
    suggestions = []
    selection_mode = False
    infos.configure(text="")
    frame_actions.pack_forget()
    toggle_champ_fams(True)  # Réafficher la barre de texte
    champ_fams.delete(0, 'end')
    champ_fams.focus_set()
    label_question.pack(pady=5)
    selection_indicator.configure(text="")
    
    # On efface les suggestions précédentes
    for label in labels_suggestions:
        label.destroy()
    labels_suggestions.clear()

def on_key_press(event):
    global suggestions, selection_mode, compte_actuel
    
    # Gestion des actions rapides si compte sélectionné
    if compte_actuel and event.keysym.isdigit():
        num = int(event.keysym)
        if 1 <= num <= 4:
            executer_action(num)
            return "break"
        return
    
    # Gestion normale si aucun compte sélectionné
    if event.keysym == "Return":
        if selection_mode:
            selection_mode = False
            champ_fams.delete(0, 'end')
        elif champ_fams.get().strip():
            selection_mode = True
            champ_fams.delete(0, 'end')
        afficher_suggestions()  # Mettre à jour l'affichage
        return "break"
    
    if selection_mode and event.keysym.isdigit():
        num = int(event.keysym)
        if num == 0:
            reset_recherche()
        elif 1 <= num <= len(suggestions):
            afficher_infos(suggestions[num-1])
        return "break"
    
    if not selection_mode and champ_fams.winfo_ismapped():
        app.after(10, update_suggestions)

def update_suggestions():
    global suggestions
    texte = champ_fams.get()
    suggestions = chercher_fams(texte)
    afficher_suggestions()

# Configuration des événements
champ_fams.bind("<Key>", on_key_press)
app.bind("<FocusIn>", lambda e: champ_fams.focus_set() if champ_fams.winfo_ismapped() else None)

app.mainloop()
conn.close()
