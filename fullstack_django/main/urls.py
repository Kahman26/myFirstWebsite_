from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60 * 15)(views.index)),
    path('about', views.about),
    path('roulette', views.roulette),
    path('test', views.test),
    path('map_test', views.map_test),

]