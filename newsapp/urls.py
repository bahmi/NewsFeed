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


]