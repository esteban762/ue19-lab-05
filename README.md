# UE19 - Lab 05 : Application Python interrogeant une API publique

Cette application Python 3 interroge l'API publique **Cat Facts** et affiche un fait aléatoire sur les chats.  
Elle utilise la librairie **requests** et peut être exécutée localement ou dans un conteneur Docker.

---

## 🐾 Fonctionnalités

- Interrogation de l’API **Cat Facts** : https://catfact.ninja/fact
- Affichage d’un fait aléatoire sur les chats
- Exécutable localement via Python ou dans Docker

---

## ⚙️ Installation et utilisation locale

### 1. Cloner le repository

```bash
git clone https://github.com/<votre-nom>/ue19-lab-05.git
cd ue19-lab-05

py -m venv venv (or python -m venv venv, dépendant si cest le launcher ou non)
.\venv\Scripts\activate
```

### 2. Sur Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Lancer l’application

```bash
python app.py
```

## Utilisation avec Docker

### 1. Installer Docker Desktop

Télécharge et installe Docker Desktop : https://www.docker.com/products/docker-desktop/

### 2. Construire l’image Docker

Dans le dossier du projet (où se trouve le Dockerfile)

```bash
docker build -t ue19-lab05 .
```

### 3. Lancer le conteneur

```bash
docker run --rm ue19-lab05
```
