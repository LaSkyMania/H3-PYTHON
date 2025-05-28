from django.shortcuts import render, redirect, get_object_or_404
from .models import Country
from .models import City
from .models import Film
from datetime import datetime
from .models import CustomUser
import bcrypt

def index(request):
    if not request.session.get('user_id'):
        return redirect('login')
    
    hour = datetime.now().strftime('%H:%M:%S')
    return render(request, 'sakila/index.html', {'hour': hour })

def country_list(request):
    if not request.session.get('user_id'):
        return redirect('login')

    countries = Country.objects.all()
    return render(request, 'sakila/country_list.html', {'countries': countries})

def country_detail(request, pk):
    if not request.session.get('user_id'):
        return redirect('login')
    
    country = get_object_or_404(Country, pk=pk)
    return render(request, 'sakila/country_detail.html', {'country': country})

def city_list(request):
    if not request.session.get('user_id'):
        return redirect('login')
    
    cities = City.objects.all()
    return render(request, 'sakila/city_list.html', {'cities': cities})

def city_detail(request, pk):
    if not request.session.get('user_id'):
        return redirect('login')
    
    city = get_object_or_404(City, pk=pk)
    return render(request, 'sakila/city_detail.html', {'city': city})

def film_list(request):
    if not request.session.get('user_id'):
        return redirect('login')
    
    films = Film.objects.all()
    return render(request, 'sakila/film_list.html', {'films': films})

def film_detail(request, pk):
    
    film = get_object_or_404(Film, pk=pk)
    return render(request, 'sakila/film_detail.html', {'film': film})

def login_view(request):
    error = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = CustomUser.objects.get(username=username)
            if bcrypt.checkpw(password.encode(), user.password.encode()):
                request.session['user_id'] = user.user_id
                return redirect('index')
            else:
                error = "Mot de passe incorrect."
        except CustomUser.DoesNotExist:
            error = "Utilisateur introuvable."

    return render(request, 'sakila/login.html', {'error': error})