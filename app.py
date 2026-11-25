#!/usr/bin/env python3
"""Affiche une blague aléatoire en interrogeant l'Official Joke API.

API utilisée : https://official-joke-api.appspot.com (publique, sans authentification).
"""

import argparse
import sys

import requests

BASE_URL = "https://official-joke-api.appspot.com"
TIMEOUT = 10  # secondes


def get_joke(joke_type=None):
    """Retourne un dictionnaire décrivant une blague (setup + punchline)."""
    if joke_type:
        url = f"{BASE_URL}/jokes/{joke_type}/random"
    else:
        url = f"{BASE_URL}/random_joke"

    response = requests.get(url, timeout=TIMEOUT)
    response.raise_for_status()
    data = response.json()

    # Le endpoint /jokes/<type>/random renvoie une liste d'un élément.
    if isinstance(data, list):
        if not data:
            raise ValueError(f"Aucune blague trouvée pour le type '{joke_type}'.")
        data = data[0]
    return data


def main():
    parser = argparse.ArgumentParser(description="Affiche une blague aléatoire.")
    parser.add_argument(
        "-t",
        "--type",
        choices=["general", "programming", "knock-knock", "dad"],
        help="type de blague souhaité (par défaut : aléatoire)",
    )
    args = parser.parse_args()

    try:
        joke = get_joke(args.type)
    except requests.exceptions.RequestException as err:
        print(f"Erreur lors de l'appel à l'API : {err}", file=sys.stderr)
        sys.exit(1)
    except ValueError as err:
        print(f"Erreur : {err}", file=sys.stderr)
        sys.exit(1)

    print(f"[{joke.get('type', '?')}]")
    print(joke["setup"])
    print(f"  -> {joke['punchline']}")


if __name__ == "__main__":
    main()
