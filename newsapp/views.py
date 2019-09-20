from django.shortcuts import render
from decouple import config
from newsapi import NewsApiClient

api_request = NewsApiClient(api_key=config('api_key'))

def home(request):
    technology_src = api_request.get_sources(category='technology', language='en')
    sports_src = api_request.get_sources(category='sports', language='en')
    business_src = api_request.get_sources(category='business', language='en')
    entertainment_src = api_request.get_sources(category='entertainment', language='en')

    return render(request, 'home.html', {'technology_src': technology_src,
                                         'sports_src': sports_src,
                                         'business_src': business_src,
                                         'entertainment_src': entertainment_src,
                                         })

def ars_technica(request):
    page_title = 'Ars Technica'
    ars_technica = api_request.get_top_headlines(sources='ars-technica', language='en')
    return render(request, 'ars_technica.html', {'ars_technica': ars_technica, 'page_title': page_title})

def crypto_coins_news(request):
    page_title = 'Crypto Coins News'
    crypto_coins_news = api_request.get_top_headlines(sources='crypto-coins-news', language='en')
    return render(request, 'crypto_coins_news.html', {'crypto_coins_news': crypto_coins_news,
                                                      'page_title': page_title})

def engadget(request):
    page_title = 'Engadget'
    engadget = api_request.get_top_headlines(sources='engadget', language='en')
    return render(request, 'engadget.html', {'engadget': engadget,
                                             'page_title': page_title})

def hacker_news(request):
    page_title = 'Hacker News'
    hacker_news = api_request.get_top_headlines(sources='hacker-news', language='en')
    return render(request, 'hacker_news.html', {'hacker_news': hacker_news,
                                                'page_title': page_title})

def recode(request):
    page_title = 'Recode'
    recode = api_request.get_top_headlines(sources='recode', language='en')
    return render(request, 'recode.html', {'recode': recode,
                                           'page_title': page_title})

def techcrunch(request):
    page_title = 'TechCrunch'
    techcrunch = api_request.get_top_headlines(sources='techcrunch', language='en')
    return render(request, 'techcrunch.html', {'techcrunch': techcrunch,
                                               'page_title': page_title})

def techradar(request):
    page_title = 'TechRadar'
    techradar = api_request.get_top_headlines(sources='techradar', language='en')
    return render(request, 'techradar.html', {'techradar': techradar,
                                              'page_title': page_title})

def the_next_web(request):
    page_title = 'The Next Web'
    the_next_web = api_request.get_top_headlines(sources='the-next-web', language='en')
    return render(request, 'the_next_web.html', {'the_next_web': the_next_web,
                                                 'page_title': page_title})

def the_verge(request):
    page_title = 'The Verge'
    the_verge = api_request.get_top_headlines(sources='the-verge', language='en')
    return render(request, 'the_verge.html', {'the_verge': the_verge,
                                               'page_title': page_title})

def wired(request):
    page_title = 'Wired'
    wired = api_request.get_top_headlines(sources='wired', language='en')
    return render(request, 'wired.html', {'wired': wired,
                                               'page_title': page_title})











