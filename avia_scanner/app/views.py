import time
import random

from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache

from .models import City
from .forms import SearchTicket


def ticket_page_view(request):
    template = 'app/ticket_page.html'

    context = {
        'form': SearchTicket()
    }

    return render(request, template, context)


def cities_lookup(request):
    term = request.GET.get('term')
    cached = cache.get('cities')
    if cached is None:
        cities = []
        for city in City.objects.only('name'):
            cities.append(str(city))
        cache.set('cities', cities)
    else:
        cities = cached

    city_filter = list(filter(lambda city: term in city, cities))

    results = city_filter
    return JsonResponse(results, safe=False)