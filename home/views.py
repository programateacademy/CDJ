from django.http import Http404, JsonResponse
from django.shortcuts import render
from .models import Aboutus, Collaborators, Consejos, Documents
from django.db.models import Q
from login.models import Post
from django.urls import reverse

# traer todos los consejos al home

def home(request):
    consejos = Consejos.objects.all()
    latest_post = Post.objects.last() 
    if latest_post:
        all_posts = Post.objects.exclude(id=latest_post.id)
    else:
        all_posts = []
        latest_post = []
    context = {'consejos': consejos, 'latest_post': latest_post, 'all_posts': all_posts}
    return render(request, 'home.html', context)

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
    results = [{'name': c.name, 'logo': c.logo.url, 'description': c.description, 'email': c.email, 'type_consejo': c.type_consejo, 'id': c.id} for c in consejos]
    return JsonResponse({'results': results})

#Vista para cada consejo

def detalle_consejo(request, consejo_id):
    try:
        consejo = Consejos.objects.get(id=consejo_id)
        collaborators = Collaborators.objects.filter(consejo=consejo)
        documents = Documents.objects.filter(consejo=consejo)
        aboutus = Aboutus.objects.filter(consejo=consejo).first()
        all_posts = Post.objects.filter(consejo=consejo)
        latest_post = all_posts.last()

        if latest_post:
            all_posts = all_posts.exclude(id=latest_post.id)
        else:
            all_posts = []
            latest_post=[]
    

    except Consejos.DoesNotExist:
        raise Http404("El consejo no existe")
    return render(request, 'council.html', {'consejo': consejo, 'collaborators': collaborators, 'documents': documents,'aboutus':aboutus,'latest_post': latest_post,'all_posts': all_posts})

# Vista para las noticias
def post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404("La noticia no existe")
    return render(request, 'news.html', {'post': post})
