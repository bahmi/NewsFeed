from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
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
]