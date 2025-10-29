import requests
from django.shortcuts import render

def home(request):
 if request.method == "GET":
  url = "http://127.0.0.1:8001/api/cardapio/"
  response = requests.get(url)
  if response.status_code == 200:
   texto = response.json()
  else:
   texto = []
  return render(request,"site.html",{"texto":texto})  
