# 📅 calendar_RPI — Affichage du calendrier Outlook sur Raspberry Pi

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge)
![Selenium](https://img.shields.io/badge/Selenium-4%2B-43B02A?style=for-the-badge)
![RaspberryPi](https://img.shields.io/badge/Raspberry_Pi-4%2B-C51A4A?style=for-the-badge)
![Licence](https://img.shields.io/badge/Licence-MIT-green?style=for-the-badge)

Script Python affichant automatiquement le calendrier Outlook (Office 365) en plein écran sur un Raspberry Pi. Ouvre un navigateur Chromium en mode kiosk, se connecte automatiquement au compte Microsoft et affiche la vue semaine de travail en continu.

---

## Fonctionnalités

- Connexion automatique au compte Microsoft 365
- Affichage en plein écran (mode kiosk) du calendrier Outlook
- Gestion automatique de la session (mémorisation de connexion)
- Boucle infinie pour maintenir l'affichage sans intervention
- Compatible Raspberry Pi avec Chromium (via `undetected-chromedriver`)

---

## Prérequis

- Python 3.8 ou supérieur
- Raspberry Pi avec interface graphique (Raspberry Pi OS Desktop)
- Chromium installé sur le Raspberry Pi
- ChromeDriver compatible avec la version de Chromium installée

---

## Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/titithen00b/calendar_RPI.git
cd calendar_RPI
```

### 2. Installer les dépendances Python

```bash
pip install -r requirements.txt
```

### 3. Télécharger ChromeDriver

Télécharger la version de ChromeDriver correspondant à la version de Chromium installée sur le Raspberry Pi :

- Chromium standard : [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)
- Chromium via Electron : [https://github.com/electron/electron/releases](https://github.com/electron/electron/releases)

Vérifier la version de Chromium installée :

```bash
chromium-browser --version
```

Placer l'exécutable `chromedriver` dans le même dossier que les scripts.

---

## Configuration

Ouvrir `calendar_rpi.py` et renseigner les informations de connexion Microsoft 365 :

```python
email = "mon.email@domaine.com"
mot_de_passe = "mon_mot_de_passe"
```

> **Sécurité :** Ne jamais committer ce fichier avec les vrais identifiants. Utiliser des variables d'environnement ou un fichier `.env` en production.

---

## Utilisation

### Lancement manuel

```bash
python3 calendar_rpi.py
```

Le script :
1. Ouvre Chromium en mode kiosk (plein écran)
2. Navigue vers la vue semaine de travail Outlook
3. Saisit automatiquement l'email et le mot de passe
4. Reste affiché en boucle infinie

### Démarrage automatique au boot

Ajouter au fichier `~/.config/lxsession/LXDE-pi/autostart` :

```bash
@python3 /chemin/vers/calendar_rpi.py
```

---

## Fichiers du projet

| Fichier | Description |
|---------|-------------|
| `calendar_rpi.py` | Script principal avec connexion automatique Microsoft 365 |
| `calendar.py` | Version alternative simplifiée |
| `requirements.txt` | Dépendances Python |

---

## Licence

MIT © Titithen00b
