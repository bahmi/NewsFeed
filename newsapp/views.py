from django.shortcuts import render
from decouple import config
from newsapi import NewsApiClient

# Create your views here.
def home(request):
    api_request = NewsApiClient(api_key=config('api_key'))
    technology_src = api_request.get_sources(category='technology', language='en')
    sports_src = api_request.get_sources(category='sports', language='en')
    business_src = api_request.get_sources(category='business', language='en')
    entertainment_src = api_request.get_sources(category='entertainment', language='en')

    return render(request, 'home.html', {'technology_src': technology_src,
                                         'sports_src': sports_src,
                                         'business_src': business_src,
                                         'entertainment_src': entertainment_src,
                                         })