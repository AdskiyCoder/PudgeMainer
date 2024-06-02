from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('auth', views.auth, name='auth'),
    path('nepoker', views.nepoker, name='nepoker'),
    path('TwentyOne', views.TwentyOne, name='TwentyOne'),
    path('roulette', views.roulette, name='roulette'),
]
