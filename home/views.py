from django.http import JsonResponse
from django.shortcuts import render
from .models import Consejos
from django.db.models import Q

# traer todos los consejos al home

def home(request):
    consejos = Consejos.objects.all()
    return render(request, 'home.html', {'consejos': consejos})

# Traer solo los curules especiales

def curul_consejos(request):
    curul_consejos = Consejos.objects.filter(type_consejo='Curul')
    return render(request, 'consejos_locales.html', {'curul_consejos': curul_consejos})

# Traer solo los consejos locales 

def consejos_locales(request):
    consejos_locales = Consejos.objects.filter(type_consejo='Local')
    return render(request, 'consejos_locales.html', {'consejos_locales': consejos_locales})

# Buscar solo los consejos locales 

def search_consejos(request):
    query = request.GET.get('q', '')
    consejos = Consejos.objects.filter(name__icontains=query, type_consejo='Local')
    results = [{'name': c.name, 'logo': c.logo.url, 'description': c.description, 'email': c.email, 'type_consejo': c.type_consejo, 'user': c.user.username} for c in consejos]
    return JsonResponse({'results': results})