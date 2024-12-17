import requests
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from dotenv import load_dotenv
import os


load_dotenv()


NEWS_API_URL = os.getenv("NEWS_API_URL")

@require_GET  
def fetch_news(request):
    try:
        response = requests.get(NEWS_API_URL)
        
        response.raise_for_status()
   
        data = response.json()

        return JsonResponse(data, safe=False, status=200)

    except requests.exceptions.RequestException as e:
        
        return JsonResponse({"error": str(e)}, status=500)
