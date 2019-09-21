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

# technology news sources
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

def bbc_sport(request):
    page_title = 'BBC Sport'
    bbc_sport = api_request.get_top_headlines(sources='bbc-sport', language='en')
    return render(request, 'bbc_sport.html', {'bbc_sport': bbc_sport,
                                              'page_title': page_title})

def bleacher_report(request):
    page_title = 'Bleacher Report'
    bleacher_report = api_request.get_top_headlines(sources='bleacher-report', language='en')
    return render(request, 'bleacher_report.html', {'bleacher_report': bleacher_report,
                                                    'page_title': page_title})

def espn(request):
    page_title = 'ESPN'
    espn = api_request.get_top_headlines(sources='espn', language='en')
    return render(request, 'espn.html', {'espn': espn,
                                         'page_title': page_title})

def espn_cric_info(request):
    page_title = 'ESPN Cric Info'
    espn_cric_info = api_request.get_top_headlines(sources='espn-cric-info', language='en')
    return render(request, 'espn_cric_info.html', {'espn_cric_info': espn_cric_info,
                                                   'page_title': page_title})

def football_italia(request):
    page_title = 'Football Italia'
    football_italia = api_request.get_top_headlines(sources='football-italia', language='en')
    return render(request, 'football_italia.html', {'football_italia': football_italia,
                                                    'page_title': page_title})

def four_four_two(request):
    page_title = 'FourFourTwo'
    four_four_two = api_request.get_top_headlines(sources='four-four-two', language='en')
    return render(request, 'four_four_two.html', {'four_four_two': four_four_two,
                                                  'page_title': page_title})

def fox_sports(request):
    page_title = 'Fox Sports'
    fox_sports = api_request.get_top_headlines(sources='fox-sports', language='en')
    return render(request, 'fox_sports.html', {'fox_sports': fox_sports,
                                               'page_title': page_title})

def nfl_news(request):
    page_title = 'NFL News'
    nfl_news = api_request.get_top_headlines(sources='nfl-news', language='en')
    return render(request, 'nfl_news.html', {'nfl_news': nfl_news,
                                             'page_title': page_title})

def nhl_news(request):
    page_title = 'NHL News'
    nhl_news = api_request.get_top_headlines(sources='nhl-news', language='en')
    return render(request, 'nhl_news.html', {'nhl_news': nhl_news,
                                             'page_title': page_title})

def talksport(request):
    page_title = 'TalkSport'
    talksport = api_request.get_top_headlines(sources='talksport', language='en')
    return render(request, 'talksport.html', {'talksport': talksport,
                                              'page_title': page_title})

def the_sport_bible(request):
    page_title = 'The Sport Bible'
    the_sport_bible = api_request.get_top_headlines(sources='the-sport-bible', language='en')
    return render(request, 'the_sport_bible.html', {'the_sport_bible': the_sport_bible,
                                                    'page_title': page_title})

def australian_financial_review(request):
    page_title = 'Australian Financial Review'
    australian_financial_review = api_request.get_top_headlines(sources='australian-financial-review', language='en')
    return render(request, 'australian_financial_review.html', {'australian_financial_review': australian_financial_review,
                                                                'page_title': page_title})

def bloomberg(request):
    page_title = 'Bloomberg'
    bloomberg = api_request.get_top_headlines(sources='bloomberg', language='en')
    return render(request, 'bloomberg.html', {'bloomberg': bloomberg,
                                              'page_title': page_title})

def business_insider(request):
    page_title = 'Business Insider'
    business_insider = api_request.get_top_headlines(sources='business-insider', language='en')
    return render(request, 'business_insider.html', {'business_insider': business_insider,
                                                     'page_title': page_title})

def business_insider_uk(request):
    page_title = 'Business Insider (UK)'
    business_insider_uk = api_request.get_top_headlines(sources='business-insider-uk', language='en')
    return render(request, 'business_insider_uk.html', {'business_insider_uk': business_insider_uk,
                                                        'page_title': page_title})

def cnbc(request):
    page_title = 'CNBC'
    cnbc = api_request.get_top_headlines(sources='cnbc', language='en')
    return render(request, 'cnbc.html', {'cnbc': cnbc,
                                         'page_title': page_title})

def financial_post(request):
    page_title = 'Financial Post'
    financial_post = api_request.get_top_headlines(sources='financial-post', language='en')
    return render(request, 'financial_post.html', {'financial_post': financial_post,
                                                   'page_title': page_title})

def fortune(request):
    page_title = 'Fortune'
    fortune = api_request.get_top_headlines(sources='fortune', language='en')
    return render(request, 'fortune.html', {'fortune': fortune,
                                            'page_title': page_title})

def the_wall_street_journal(request):
    page_title = 'The Wall Street Journal'
    the_wall_street_journal = api_request.get_top_headlines(sources='the-wall-street-journal', language='en')
    return render(request, 'the_wall_street_journal.html', {'the_wall_street_journal': the_wall_street_journal,
                                                            'page_title': page_title})












