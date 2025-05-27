from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('countries/', views.country_list, name='country_list'),
    path('countries/<int:pk>/', views.country_detail, name='country_detail'),
    path('cities/', views.city_list, name='city_list'),
    path('cities/<int:pk>/', views.city_detail, name='city_detail'),
    path('films/', views.film_list, name='film_list'),
    path('films/<int:pk>/', views.film_detail, name='film_detail'),
]