from django.shortcuts import render
from .models import Task
import psycopg2
import random
import folium
from folium.plugins import MarkerCluster

con_1 = psycopg2.connect('postgresql://postgres:33Voroni@localhost/dataBase1')
cur_1 = con_1.cursor()
cur_1.execute("SELECT * FROM public.bars ORDER BY bar_id ASC")
all_bars = cur_1.fetchall()


def map_test(request):

    map = folium.Map(
        location=[56.837703, 60.597564],
        zoom_start = 14
    )

    marker_cluster = MarkerCluster().add_to(map)

    # Ниже попытка подключить иконку

    # url = "https://leafletjs.com/examples/custom-icons/{}".format
    #icon_image = 'myFirstWebsite/fullstack_django/main/static/main/img/search.png'
    icon_image = 'https://w7.pngwing.com/pngs/133/129/png-transparent-cocktail-computer-icons-restaurant-coffee-food-evening-party-angle-food-text.png'
    # shadow_image = url("leaf-shadow.png")

    icon = folium.features.CustomIcon(
        icon_image,
        icon_size=(28, 30),
        #icon_anchor=(22, 94),
        # shadow_image=shadow_image,
        # shadow_size=(50, 64),
        # shadow_anchor=(4, 62),
        # popup_anchor=(-3, -76),
    )

    folium.Marker(
        location=[56.837800, 60.596309], icon=icon, popup="Памятник Ленину"
    ).add_to(marker_cluster)

    # Выше попытка подключить иконку

    for one_bar in all_bars:
        folium.CircleMarker(
            location=[one_bar[5], one_bar[6]],
            popup=one_bar[1],
            fill_color='white',
            color='red',
            fill_opacity = 0.9
        ).add_to(marker_cluster)

    map.save("main/templates/main/map.html")

    return render(request, 'main/map.html')


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

    random_bar = random.randint(1, all_bars[len(all_bars) - 1][0])

    info_of_rand_bar = all_bars[random_bar - 1]


    return render(request, 'main/test.html', {'users': mails, 'bars': info_of_rand_bar})