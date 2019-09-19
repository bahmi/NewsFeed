from django.shortcuts import render
from decouple import config
from newsapi import NewsApiClient

# Create your views here.
def home(request):
    api_request = NewsApiClient(api_key=config('api_key'))
    business_sources = api_request.get_sources(category='business', language='en')
    return render(request, 'home.html', {'api_request':api_request, 'business_sources': business_sources})