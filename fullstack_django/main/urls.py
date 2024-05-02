from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('roulette', views.roulette),
    path('test', views.test),
    path('map_test', views.map_test),

]