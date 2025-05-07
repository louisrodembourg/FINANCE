import os
import requests
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

def test_financial_metrics_api():
    # Récupérer la clé API
    api_key = os.getenv("FINANCIAL_DATASETS_API_KEY")
    
    # Headers avec la clé API
    headers = {}
    if api_key:
        headers["X-API-KEY"] = api_key
        print("API Key found in .env")
    else:
        print("No API Key found in .env")
    
    # URL de l'API pour AAPL (qui est gratuit)
    url = "https://api.financialdatasets.ai/financial-metrics/?ticker=AAPL&report_period_lte=2024-03-01&limit=1&period=ttm"
    
    try:
        # Faire la requête
        response = requests.get(url, headers=headers)
        
        # Afficher le statut de la réponse
        print(f"\nStatus Code: {response.status_code}")
        
        # Afficher les headers de la réponse
        print("\nResponse Headers:")
        for key, value in response.headers.items():
            print(f"{key}: {value}")
        
        # Afficher le contenu de la réponse
        print("\nResponse Content:")
        print(response.text)
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_financial_metrics_api() 