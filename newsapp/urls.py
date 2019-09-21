from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.home, name='home'),
    path('sources/', RedirectView.as_view(url='/', permanent=False), name='index'),
    path('sources/ars-technica', views.ars_technica, name='ars_technica'),
    path('sources/crypto-coins-news', views.crypto_coins_news, name='crypto_coins_news'),
    path('sources/engadget', views.engadget, name='engadget'),
    path('sources/hacker-news', views.hacker_news, name='hacker_news'),
    path('sources/recode', views.recode, name='recode'),
    path('sources/techcrunch', views.techcrunch, name='techcrunch'),
    path('sources/techradar', views.techradar, name='techradar'),
    path('sources/the-next-web', views.the_next_web, name='techradar'),
    path('sources/the-verge', views.the_verge, name='the_verge'),
    path('sources/wired', views.wired, name='wired'),

    path('sources/bbc-sport', views.bbc_sport, name='bbc_sport'),
    path('sources/bleacher-report', views.bleacher_report, name='bleacher_report'),
    path('sources/espn', views.espn, name='espn'),
    path('sources/espn-cric-info', views.espn_cric_info, name='espn_cric_info'),
    path('sources/football-italia', views.football_italia, name='football_italia'),
    path('sources/four-four-two', views.four_four_two, name='four_four_two'),
    path('sources/fox-sports', views.fox_sports, name='fox_sports'),
    path('sources/nfl-news', views.nfl_news, name='nfl_news'),
    path('sources/nhl-news', views.nhl_news, name='nhl_news'),
    path('sources/talksport', views.talksport, name='talksport'),
    path('sources/the-sport-bible', views.the_sport_bible, name='the_sport_bible'),

    path('sources/australian-financial-review', views.australian_financial_review, name='australian_financial_review'),
    path('sources/bloomberg', views.bloomberg, name='bloomberg'),
    path('sources/business-insider', views.business_insider, name='business_insider'),
    path('sources/business-insider-uk', views.business_insider_uk, name='business_insider_uk'),
    path('sources/cnbc', views.cnbc, name='cnbc'),
    path('sources/financial-post', views.financial_post, name='financial_post'),
    path('sources/fortune', views.fortune, name='fortune'),
    path('sources/the-wall-street-journal', views.the_wall_street_journal, name='the_wall_street_journal'),

    path('sources/buzzfeed', views.buzzfeed, name='buzzfeed'),
    path('sources/daily-mail', views.daily_mail, name='daily_mail'),
    path('sources/entertainment-weekly', views.entertainment_weekly, name='entertainment_weekly'),
    path('sources/ign', views.ign, name='ign'),
    path('sources/mashable', views.mashable, name='mashable'),
    path('sources/mtv-news', views.mtv_news, name='mtv_news'),
    path('sources/mtv-news-uk', views.mtv_news_uk, name='mtv_news_uk'),
    path('sources/polygon', views.polygon, name='polygon'),
    path('sources/the-lad-bible', views.the_lad_bible, name='the_lad_bible'),
]