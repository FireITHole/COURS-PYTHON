import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Email:
    # Initialisation de l'objet Email
    def __init__(self, adresse_email: str, mot_de_passe: str, serveur_smtp="smtp.gmail.com", port_smtp=587):
        self.adresse_email = adresse_email
        self.mot_de_passe = mot_de_passe
        self.serveur_smtp = serveur_smtp
        self.port_smtp = port_smtp

    def envoyer_mail(self, destinataire: str, sujet: str, corps: str) -> None:
        # Création du message
        message = MIMEMultipart()
        message["From"] = self.adresse_email
        message["To"] = destinataire
        message["Subject"] = sujet

        # Ajout du corps du message
        message.attach(MIMEText(corps))

        try:
            # Connexion au serveur SMTP
            with smtplib.SMTP(host=self.serveur_smtp, port=self.port_smtp) as server:
                # Démarrage de la connexion sécurisée
                server.starttls()

                # Connexion au compte
                server.login(self.adresse_email, self.mot_de_passe)

                # Envoi du mail
                server.sendmail(self.adresse_email, destinataire, message.as_string())

            print("Email envoyé avec succès!")
        except Exception as error:
            print(f"Erreur lors de l'envoi de l'email : {error}")


# Exemple d'utilisation

