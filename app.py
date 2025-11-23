import requests

# URL de l'API Cat Facts
API_URL = "https://catfact.ninja/fact"

def get_cat_fact():
    try:
        response = requests.get(API_URL, timeout=5)  # Timeout de 5 secondes
        response.raise_for_status()  # Vérifie que la requête est OK (200)
        
        data = response.json()  # Convertit la réponse en JSON
        fact = data.get("fact", "Aucun fait trouvé.")  # Récupère le champ "fact"
        
        print("🐱 Fait sur les chats :")
        print(fact)
    
    except requests.exceptions.RequestException as e:
        print("Erreur lors de l'appel à l'API :", e)

# Point d'entrée du script
if __name__ == "__main__":
    get_cat_fact()
