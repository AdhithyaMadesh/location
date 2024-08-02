import requests
from django.shortcuts import render
from django.http import JsonResponse
from .models import IPAddress

# def store_ip(request):
#     ip = request.META.get('REMOTE_ADDR')
    
#     # Fetch additional details from ipinfo.io
#     response = requests.get(f'https://ipinfo.io/{ip}/json')
#     data = response.json()
    
#     city = data.get('city', '')
#     region = data.get('region', '')
#     country = data.get('country', '')
#     loc = data.get('loc', '')
#     org = data.get('org', '')
    
#     IPAddress.objects.create(ip=ip, city=city, region=region, country=country, loc=loc, org=org)
    
#     return JsonResponse({'status': 'success'})

def index(request):
    response = requests.get('https://ipinfo.io')
    # Parse the JSON response
    data = response.json()

    # Extract location information
    ip = data.get('ip')
    city = data.get('city')
    region = data.get('region')
    country = data.get('country')
    loc = data.get('loc')  # This gives latitude and longitude
    org = data.get('org')
    IPAddress.objects.create(ip=ip, city=city, region=region, country=country, loc=loc, org=org)
    return render(request, 'myapp/index.html')
