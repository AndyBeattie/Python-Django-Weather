#Views.py File
from json import loads
from django.shortcuts import render
from requests import api

def home(request):
    import json
    import requests

    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=10001&distance=25&API_KEY=154AF178-DDC4-46C1-8F86-5984856A7DB3")
    
    try:
        api = json.loads(api_request.content)

    except Exception as e:
        api = "Error.."

    if api[1]['AQI'] <= 25:
        pm25_index = "good"

    if api[1]['AQI'] > 25 and api[1]['AQI'] <= 50:
        pm25_index = "moderate"

    if api[1]['AQI'] > 50 and api[1]['AQI'] <= 100:
        pm25_index = "unhealthyforsensitivegroups"

    if api[1]['AQI'] > 100 and api[1]['AQI'] <= 300 :
        pm25_index = "unhealthy"

    if api[1]['AQI'] > 300 and api[1]['AQI'] <= 500:
        pm25_index = "veryunhealthy"

    if api[1]['AQI'] > 500: 
        pm25_index = "hazardous"

    return render(request,'home.html', {'api': api,'pm25_index': pm25_index})

def about(request):
    return render(request,'about.html', {})

# Create your views here.
