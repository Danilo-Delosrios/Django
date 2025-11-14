from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pruebas/', views.pruebas, name='pruebas'),
    path('template/', views.mostrar_template, name='template'),
]
