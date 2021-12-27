#Views.py File
from json import loads
from django.shortcuts import render
from requests import api

def home(request):
    import json
    import requests

    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=90001&distance=25&API_KEY=154AF178-DDC4-46C1-8F86-5984856A7DB3")
    
    try:
        api = json.loads(api_request.content)

    except Exception as e:
        api = "Error.."

    #Expand Regions
    #region PM 2.5 Quality Colour Changing Logic
    if api[0]['Category']['Name'] == 'Good':
        pm25_quality = "good"

    if api[0]['Category']['Name'] == 'Moderate':
        pm25_quality = "moderate"

    if api[0]['Category']['Name'] == 'Unhealthyforsensitivegroups':
        pm25_quality = "unhealthyforsensitivegroups"

    if api[0]['Category']['Name'] == 'Unhealthy':
        pm25_quality = "unhealthy"

    if api[0]['Category']['Name'] == 'Hazardous':
        pm25_quality = "hazardous"
    #endregion
    #region Air Quality Colour Changing Logic
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
#endregion
    
    return render(request,'home.html', {'api': api,'pm25_index': pm25_index, 'pm25_quality': pm25_quality})

def about(request):
    return render(request,'about.html', {})


