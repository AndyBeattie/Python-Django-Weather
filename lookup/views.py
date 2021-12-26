#Views.py File
from json import loads
from django.shortcuts import render

def home(request):
    import json
    import requests

    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=10001&distance=25&API_KEY=154AF178-DDC4-46C1-8F86-5984856A7DB3")
    
    try:
        api = json.loads(api_request.content)

    except Exception as e:
        api = "Error.."

    return render(request,'home.html', {'api': api})

def about(request):
    return render(request,'about.html', {})

# Create your views here.
