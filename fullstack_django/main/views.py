from django.shortcuts import render
from .models import Task
import psycopg2
import random
import folium


def map_test(request):

    russia_map = folium.Map(
        location=[37.296933,-121.9574983],
        zoom_start = 8
    )

    folium.Marker(location=[37.4074687, -122.086669], popup="Google HQ", icon=folium.Icon(color='gray')).add_to(russia_map)

    russia_map.save("main/templates/main/map1.html")

    return render(request, 'main/map1.html')


def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def roulette(request):
    return render(request, 'main/test.html')


def test(request):
    con = psycopg2.connect('postgresql://postgres:33Voroni@localhost/dataBase1')
    cur = con.cursor()
    cur.execute("SELECT * FROM public.users ORDER BY user_id ASC")
    users = cur.fetchall()

    mails_list = list()
    for i in users:
        mails_list.append(i[1])
    mails = ' '.join(mails_list)

    ###########################

    con_1 = psycopg2.connect('postgresql://postgres:33Voroni@localhost/dataBase1')
    cur_1 = con_1.cursor()
    cur_1.execute("SELECT * FROM public.bars ORDER BY bar_id ASC")
    all_bars = cur_1.fetchall()

    random_bar = random.randint(1, all_bars[len(all_bars) - 1][0])

    info_of_rand_bar = all_bars[random_bar - 1]

    ###########################



    ###########################

    return render(request, 'main/test.html', {'users': mails, 'bars': info_of_rand_bar, 'bar_map': russia_map})