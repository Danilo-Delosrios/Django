from django.shortcuts import render
from django.http import HttpResponse

def pruebas(request):
    return HttpResponse("<h1>Bienvenido a Django desde unitecnar</h1>")
def mostrar_template(request):
    return render(request, 'index.html')
def home(request):
    return render(request, 'home.html')