# 🍽️ Restaurant Manager - Django Project

## 📌 1. Titre & Description

**Restaurant Manager** est une application web développée avec Django permettant de gérer efficacement un restaurant.
Elle offre plusieurs fonctionnalités comme la gestion des menus, des commandes, des tables ainsi que l’authentification des utilisateurs.

🎯 Objectif : simplifier l’organisation quotidienne d’un restaurant à travers une interface web claire et fonctionnelle.

🔗 **Lien du projet GitHub :**
👉 https://github.com/loujain132/DJANGO

---

## ⚙️ 2. Prérequis

Avant de lancer le projet, assurez-vous d’avoir installé :

* 🐍 Python (version 3.8 ou plus)
* 📦 pip (gestionnaire de packages Python)
* 🌐 Navigateur web (Chrome, Firefox, etc.)
* (Optionnel) 🧰 Virtualenv

---

## 📥 3. Installation

### 🔹 Étapes à suivre :

```bash
# Cloner le projet
git clone https://github.com/TON_LIEN_GITHUB

# Accéder au dossier
cd restaurant_manager

# Créer un environnement virtuel
python -m venv .venv

# Activer l’environnement
# Windows :
.venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt

# Appliquer les migrations
python manage.py makemigrations
python manage.py migrate
```

---

## 🚀 4. Utilisation

### ▶️ Lancer le serveur :

```bash
python manage.py runserver
```

Puis ouvrir dans le navigateur :

http://127.0.0.1:8000/

### 🔐 Accès admin (optionnel) :

```bash
python manage.py createsuperuser
```

Puis :

http://127.0.0.1:8000/admin

---

## 🧩 Fonctionnalités

* 🔑 Authentification (login)
* 🍔 Gestion du menu
* 🧾 Gestion des commandes
* 🪑 Gestion des tables
* 📊 Interface simple et claire

---

## 👩‍💻 5. Auteurs

* **Loujain Dorrai**

---

## 💡 Remarques

Ce projet a été réalisé dans le cadre d’un apprentissage de Django.
Des améliorations possibles :

* Paiement en ligne 💳
* Dashboard avancé 📈
* API REST 🔗

---

✨ *Merci d’avoir utilisé Restaurant Manager !*
