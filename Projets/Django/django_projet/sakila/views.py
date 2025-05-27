from django.shortcuts import render, get_object_or_404
from .models import Country
from .models import City
from .models import Film
from datetime import datetime

def index(request):
    hour = datetime.now().strftime('%H:%M:%S')
    return render(request, 'sakila/index.html', {'hour': hour })

def country_list(request):
    countries = Country.objects.all()
    return render(request, 'sakila/country_list.html', {'countries': countries})

def country_detail(request, pk):
    country = get_object_or_404(Country, pk=pk)
    return render(request, 'sakila/country_detail.html', {'country': country})

def city_list(request):
    cities = City.objects.all()
    return render(request, 'sakila/city_list.html', {'cities': cities})

def city_detail(request, pk):
    city = get_object_or_404(City, pk=pk)
    return render(request, 'sakila/city_detail.html', {'city': city})

def film_list(request):
    films = Film.objects.all()
    return render(request, 'sakila/film_list.html', {'films': films})

def film_detail(request, pk):
    film = get_object_or_404(Film, pk=pk)
    return render(request, 'sakila/film_detail.html', {'film': film})