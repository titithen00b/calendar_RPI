from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
import time

# Informations de connexion
email = ""
mot_de_passe = ""

# URL de la page web à afficher
url = "https://outlook.office.com/calendar/view/workweek?path=%2fcalendar"

def afficher_page_web(url):
    # Configuration des options du navigateur pour afficher en plein écran
    options = Options()
    options.add_argument("--kiosk")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("prefs", {"credentials_enable_service": False, "profile.password_manager_enabled": False})
    # Initialisation du navigateur
    driver = webdriver.Chrome(options=options)

    # Ouverture de la page web en plein écran
    driver.get(url)

    # Attente pour laisser le temps au chargement de la page
    time.sleep(5)

    # Remplissage du champ d'email
    email_field = driver.find_element(By.NAME, "loginfmt")
    email_field.send_keys(email)

    # Clic sur le bouton suivant
    next_button = driver.find_element(By.ID, "idSIButton9")
    next_button.click()

    # Attente pour laisser le temps de charger la page suivante
    time.sleep(5)

    # Remplissage du champ de mot de passe
    password_field = driver.find_element(By.NAME, "passwd")
    password_field.send_keys(mot_de_passe)

    # Clic sur le bouton se connecter
    sign_in_button = driver.find_element(By.ID, "idSIButton9")
    sign_in_button.click()

    # Cocher la case "Ne plus afficher ce message" si elle est présente
    try:
        checkbox = driver.find_element(By.ID, "KmsiCheckboxField")
        checkbox.click()
    except:
        pass

    # Cliquer sur le bouton "Oui" si présent
    try:
        yes_button = driver.find_element(By.ID, "idSIButton9")
        yes_button.click()
    except:
        pass
# Ne pas fermer le navigateur automatiquement
    while True:
        pass

# Appel de la fonction pour afficher la page web en plein écran et se connecter
afficher_page_web(url)

