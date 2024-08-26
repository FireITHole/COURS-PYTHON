import tkinter as tk
from tkinter import ttk

# Définition de la classe Calculatrice
class Calculatrice:
    def __init__(self) -> None:
        # Initialisation de la fenêtre principale
        self.root = tk.Tk()
        self.root.geometry("300x400")
        self.root.title("Calculatrice Simple")

        # Configuration du style des boutons
        s = ttk.Style()
        s.configure("TButton", font="Arial 14")

        # Création de la zone d'affichage
        self.label_var = tk.StringVar()
        self.label = ttk.Label(self.root, font=("Arial", 14),
                               textvariable=self.label_var, anchor="e", padding="0 5 0 5")
        self.label.pack(fill="x")

        # Définition des boutons de la calculatrice
        self.buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        # Création du cadre pour les boutons
        self.button_frame = tk.Frame(self.root)

        # Initialisation des valeurs de ligne et de colonne pour le placement des boutons
        self.row_val = 0
        self.col_val = 0

        # Création et placement des boutons dans une grille
        for button in self.buttons:
            b = ttk.Button(self.button_frame, text=button,
                           style="TButton", command=lambda x=button: self.on_click(x))
            b.grid(row=self.row_val, column=self.col_val, sticky="nsew")
            self.col_val += 1
            if self.col_val > 3:
                self.col_val = 0
                self.row_val += 1

        # Configuration de la grille pour que les boutons s'étendent uniformément
        for i in range(4):
            self.button_frame.rowconfigure(i, weight=1)
            self.button_frame.columnconfigure(i, weight=1)

        # Placement du cadre des boutons dans la fenêtre principale
        self.button_frame.pack(expand=True, fill="both")

        # Liaison des touches du clavier aux fonctions de la calculatrice
        self.root.bind("<KeyPress>", lambda k: self.on_click(k.char)
                       if k.char in "0123456789+-*/=%C\b" else None)
        self.root.bind("<Return>", lambda _: self.on_click("="))

        # Lancement de la boucle principale de l'interface graphique
        self.root.mainloop()

    # Fonction appelée lors du clic sur un bouton
    def on_click(self, text: str) -> None:
        if text == "=":
            try:
                # Évaluation de l'expression mathématique et affichage du résultat
                result = eval(self.label_var.get())
                self.label_var.set(result)
            except Exception:
                # Affichage d'un message d'erreur en cas d'exception
                self.label_var.set("Erreur")
        elif text == "C":
            # Réinitialisation de la zone d'affichage
            self.label_var.set("")
        elif text == "\b":
            # Suppression du dernier caractère de l'expression
            self.label_var.set(self.label_var.get()[:-1])
        else:
            # Ajout du texte du bouton à l'expression actuelle
            if self.label_var.get() == "Erreur":
                self.label_var.set("")
            self.label_var.set(self.label_var.get() + text)


# Exécution de la calculatrice si ce fichier est exécuté directement
if __name__ == "__main__":
    Calculatrice()
