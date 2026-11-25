# ue19-lab-05

Petite application Python 3 qui interroge l'API publique
[Official Joke API](https://official-joke-api.appspot.com) (sans authentification)
avec la librairie [requests](https://docs.python-requests.org/en/latest/index.html)
et affiche une blague dans le terminal.

## Fonctionnalités

- Affiche une blague aléatoire (type, question et chute).
- Option `-t` / `--type` pour choisir la catégorie : `general`, `programming`, `knock-knock`, `dad`.
- Gestion des erreurs réseau (timeout, API indisponible, ...) avec un message clair et un code de sortie non nul.

## Prérequis

- Python 3.8 ou plus récent **ou** Docker

## Installation et lancement en local

```bash
git clone https://github.com/esteban762/ue19-lab-05.git
cd ue19-lab-05

python3 -m venv venv
source venv/bin/activate        # Windows : venv\Scripts\activate
pip install -r requirements.txt

python app.py                   # blague aléatoire
python app.py --type programming
```

## Lancement avec Docker

```bash
docker build -t ue19-lab-05 .

docker run --rm ue19-lab-05                      # blague aléatoire
docker run --rm ue19-lab-05 --type programming   # blague de programmation
```

## Exemple de sortie

```
[programming]
Why do programmers prefer dark mode?
  -> Because light attracts bugs.
```

## Structure du projet

| Fichier            | Rôle                                          |
|--------------------|-----------------------------------------------|
| `app.py`           | Programme qui interroge l'API                 |
| `requirements.txt` | Dépendances Python                            |
| `Dockerfile`       | Image du conteneur qui exécute `app.py`       |
| `README.md`        | Documentation                                 |
