from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('thanks/', views.thanks, name='thanks'),
    path('services/', views.services, name='services'),
    path('projects/', views.projects, name='projects'),
    path('contacts/', views.contact, name='contacts'),
    path('it/', views.it_services, name='it'),
]