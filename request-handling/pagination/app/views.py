from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import urllib.parse
import csv
from app.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    with open(BUS_STATION_CSV, newline='', encoding='cp1251') as csvfile:
        stations_data = list(csv.DictReader(csvfile))
        paginator = Paginator(stations_data, 10)

    current_page = request.GET.get('page') or 1
    bus_station = paginator.page(current_page)

    if paginator.page(current_page).has_next():
        next_page_num = bus_station.next_page_number()
        next_page_url = reverse('bus_stations') + '?' + urllib.parse.urlencode({'page': next_page_num})
    else:
        next_page_url = None

    if paginator.page(current_page).has_previous():
        prev_page_num = bus_station.previous_page_number()
        prev_page_url = reverse('bus_stations') + '?' + urllib.parse.urlencode({'page': prev_page_num})
    else:
        prev_page_url = None

    return render_to_response('index.html', context={
        'bus_stations': bus_station,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })

