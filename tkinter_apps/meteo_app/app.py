import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests
from datetime import datetime
from os import path

# Classe principale de l'application


class App:
    def __init__(self):
        self.root: tk.Tk  # On déclare le type de la variable root pour l'intellisense
        # Gestion de la fermeture de la fenêtre
        self.root.protocol("WM_DELETE_WINDOW", self.custom_exit)

    # Méthode pour gérer la fermeture personnalisée de l'application
    def custom_exit(self):
        if messagebox.askyesno("Fermeture", "Voulez-vous vraiment fermer ?"):
            try:
                self.root.after_cancel(self.id_after)
            except AttributeError:
                pass
            self.root.destroy()
            exit()

    # Méthode pour centrer la fenêtre sur l'écran
    def center_screen(self, window_width: int, window_height: int):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        self.root.geometry(f"{window_width}x{
                           window_height}+{x_cordinate}+{y_cordinate}")

# Classe pour la sélection de la ville


class SelectionVille(App):
    def __init__(self):
        self.root = tk.Tk()
        self.center_screen(300, 350)
        self.root.iconbitmap(path.join(path.dirname(__file__), "icon.ico"))
        self.root.title("Selection de la ville")
        self.root.resizable(False, False)
        super().__init__()

        # Création du cadre principal
        self.frame = ttk.Frame(self.root, padding="10 10 10 10")
        self.frame.pack(expand=True, anchor="center")

        # Label pour inviter l'utilisateur à entrer le nom d'une ville
        ttk.Label(self.frame, text="Entrez le nom d'une ville",
                  font=("Arial", 14), padding="10 10 10 10").pack()

        # Champ de saisie pour le nom de la ville
        self.ville_var = tk.StringVar()
        self.ville_entry = ttk.Entry(
            self.frame, width=30, textvariable=self.ville_var)
        self.ville_entry.pack(pady=10)
        self.ville_entry.focus()

        # Bouton pour valider la saisie
        self.valider = ttk.Button(
            self.frame, text="Valider", command=self.get_meteo, state="disabled")
        self.valider.pack()

        # Activation du bouton Valider lorsque du texte est saisi
        self.ville_entry.bind("<Return>", lambda _: self.get_meteo())
        self.ville_var.trace_add("write", lambda *_: self.valider.configure(
            state="normal" if self.ville_var.get() != "" else "disabled"))

        self.root.mainloop()

    # Méthode pour obtenir les données météo de la ville saisie
    def get_meteo(self):
        ville = self.ville_var.get()

        if ville == "":
            messagebox.showerror("Erreur", "Veuillez entrer une ville")
            return

        try:
            lat, lon, ville_geoloc, state = self.get_ville(ville)
        except (IndexError, KeyError):
            messagebox.showerror("Erreur", "Ville introuvable")
            self.ville_var.set("")
            return

        self.root.destroy()
        Meteo(lat, lon, ville_geoloc, state)

    # Méthode pour obtenir les coordonnées géographiques de la ville
    def get_ville(self, ville: str) -> tuple[float, float, str, str]:
        GEOLOC_API_KEY = "b8b76e4363b5ff75a681437a92f3ab0e"
        GEOLOC_URL = "http://api.openweathermap.org/geo/1.0/direct"
        GEOLOC_PARAMS = {"q": ville, "appid": GEOLOC_API_KEY}
        geoloc_req = requests.get(GEOLOC_URL, params=GEOLOC_PARAMS)
        geoloc_dict = geoloc_req.json()

        dictionnaire_data = geoloc_dict[0]
        return dictionnaire_data["lat"], dictionnaire_data["lon"], dictionnaire_data["local_names"]["fr"], dictionnaire_data.get("state", None)

# Classe pour afficher les données météo


class Meteo(App):
    def __init__(self, lat: float, lon: float, ville: str, state: str):
        self.lat = lat
        self.lon = lon
        self.ville = ville
        self.state = state
        self.root = tk.Tk()
        self.center_screen(425, 200)
        self.root.iconbitmap(path.join(path.dirname(__file__), "icon.ico"))
        self.root.resizable(False, False)
        self.root.title("Chargement...")
        super().__init__()

        # Création des cadres pour l'affichage des données
        self.frame = ttk.Frame(self.root)
        self.frame.pack(expand=True, anchor="center", fill="both")

        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)

        self.frame_w = ttk.Frame(self.frame, padding="10 10 10 10")
        self.frame_w.grid(row=0, column=0)

        self.frame_e = ttk.Frame(self.frame, padding="10 10 10 10")
        self.frame_e.grid(row=0, column=1)

        self.frame_s = ttk.Frame(self.frame, padding="10 10 10 10")
        self.frame_s.grid(row=1, column=0, columnspan=2)

        # Labels pour afficher les données météo
        self.ville_label = ttk.Label(
            self.frame_w, font=("Arial", 14), padding="0 0 0 10")
        self.ville_label.pack()

        self.temperature_label = ttk.Label(self.frame_w)
        self.temperature_label.pack()

        self.temperature_apparente_label = ttk.Label(self.frame_w)
        self.temperature_apparente_label.pack()

        self.humidite_label = ttk.Label(self.frame_w)
        self.humidite_label.pack()

        self.vent_label = ttk.Label(self.frame_w)
        self.vent_label.pack()

        self.precipitation_label = ttk.Label(self.frame_w)
        self.precipitation_label.pack()

        # Combobox pour choisir le système d'unités (métrique ou impérial)
        self.choix_systeme_var = tk.StringVar(value="Métrique")
        self.choix_systeme = ttk.Combobox(self.frame_s, values=[
                                          "Métrique", "Impérial"], textvariable=self.choix_systeme_var, justify="center", state="readonly")
        self.choix_systeme.pack()

        self.choix_systeme.bind("<<ComboboxSelected>>", self.convertir)

        # Cadre pour les boutons
        self.frame_boutons = ttk.Frame(self.frame_e)
        self.frame_boutons.pack(expand=True, anchor="center")

        self.derniere_maj_label = ttk.Label(self.frame_boutons)
        self.derniere_maj_label.pack(pady=(0, 10))

        self.bouton_actualiser = ttk.Button(
            self.frame_boutons, text="Actualiser", command=lambda: self.get_data(recursive=False))
        self.bouton_actualiser.pack(fill="x", pady=(0, 10))

        self.bouton_changer_ville = ttk.Button(
            self.frame_boutons, text="Changer de ville", command=self.changer_ville)
        self.bouton_changer_ville.pack(fill="x")

        self.quitter = ttk.Button(
            self.frame_boutons, text="Quitter", command=self.custom_exit)
        self.quitter.pack(fill="x")

        self.get_data()

        self.root.mainloop()

    # Méthode pour obtenir les données météo
    def get_data(self, recursive=True):
        WEATHER_URL = "https://api.open-meteo.com/v1/forecast"
        WEATHER_PARAMS = {
            "metric": {
                "latitude": self.lat,
                "longitude": self.lon,
                "current": [
                    "temperature_2m",
                    "relativehumidity_2m",
                    "apparent_temperature",
                    "precipitation",
                    "windspeed_10m",
                ],
            },
            "imperial": {
                "latitude": self.lat,
                "longitude": self.lon,
                "temperature_unit": "fahrenheit",
                "wind_speed_unit": "mph",
                "precipitation_unit": "inch",
                "current": [
                    "temperature_2m",
                    "relativehumidity_2m",
                    "apparent_temperature",
                    "precipitation",
                    "windspeed_10m",
                ],
            }
        }

        self.data = {}
        for system_name, system_params in WEATHER_PARAMS.items():
            meteo_req = requests.get(WEATHER_URL, params=system_params)
            meteo_dict = meteo_req.json()

            self.data[system_name] = meteo_dict["current"]

        self.root.title(f"Météo de {self.ville}{
                        f', {self.state}' if self.state else ''}")
        self.ville_label["text"] = f"Météo de {self.ville}"

        # Affichage des données en fonction du système d'unités choisi
        if self.choix_systeme_var.get() == "Impérial":
            self.temperature_label["text"] = f"Température : {
                self.data['imperial']['temperature_2m']}°F"
            self.temperature_apparente_label["text"] = f"Température apparente : {
                self.data['imperial']['apparent_temperature']}°F"
            self.vent_label["text"] = f"Vitesse du vent : {
                self.data['imperial']['windspeed_10m']} mph"
            self.precipitation_label["text"] = f"Precipitation : {
                self.data['imperial']['precipitation']} in"
        else:
            self.temperature_label["text"] = f"Température : {
                self.data['metric']['temperature_2m']}°C"
            self.temperature_apparente_label["text"] = f"Température apparente : {
                self.data['metric']['apparent_temperature']}°C"
            self.vent_label["text"] = f"Vitesse du vent : {
                self.data['metric']['windspeed_10m']} km/h"
            self.precipitation_label["text"] = f"Precipitation : {
                self.data['metric']['precipitation']} mm"

        self.humidite_label["text"] = f"Humidité : {
            self.data['metric']['relativehumidity_2m']}%"

        self.derniere_maj_label["text"] = f"Dernière mise à jour : {
            datetime.now().strftime('%H:%M:%S')}"

        if recursive:
            self.id_after = self.root.after(5000, self.get_data)

    # Méthode pour convertir les unités
    def convertir(self, _):
        if self.choix_systeme_var.get() == "Impérial":
            self.temperature_label["text"] = f"Température : {
                self.data['imperial']['temperature_2m']}°F"
            self.temperature_apparente_label["text"] = f"Température apparente : {
                self.data['imperial']['apparent_temperature']}°F"
            self.vent_label["text"] = f"Vitesse du vent : {
                self.data['imperial']['windspeed_10m']} mph"
            self.precipitation_label["text"] = f"Precipitation : {
                self.data['imperial']['precipitation']} in"
        else:
            self.temperature_label["text"] = f"Température : {
                self.data['metric']['temperature_2m']}°C"
            self.temperature_apparente_label["text"] = f"Température apparente : {
                self.data['metric']['apparent_temperature']}°C"
            self.vent_label["text"] = f"Vitesse du vent : {
                self.data['metric']['windspeed_10m']} km/h"
            self.precipitation_label["text"] = f"Precipitation : {
                self.data['metric']['precipitation']} mm"

    # Méthode pour changer de ville
    def changer_ville(self):
        try:
            self.root.after_cancel(self.id_after)
        except AttributeError:
            pass

        self.root.destroy()
        SelectionVille()


# Point d'entrée de l'application
if __name__ == "__main__":
    SelectionVille()
