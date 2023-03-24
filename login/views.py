from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm, DocumentForm, BannerForm, AboutUsForm, CollaboratorForm
from home.models import Documents, Banner, Aboutus, Consejos, Collaborators
import os
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate

def panel_admin(request):
    posts = Post.objects.filter(user=request.user) 
    documents = Documents.objects.filter(user=request.user)
    banners = Banner.objects.filter(user=request.user)
    about = Aboutus.objects.filter(user=request.user)
    collaborators = Collaborators.objects.filter(user=request.user)
    context = {'posts':posts, 'documents': documents, 'banners': banners, 'aboutus': about, 'collaborators': collaborators}
    return render(request, 'panel_admin.html', context)

def create_post(request):
    form = PostForm()
    type_form = 1
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            consejo = Consejos.objects.get(user=request.user)
            new_post.consejo = consejo
            new_post.save()
            return redirect('login:panel_admin')
        
    context={'form':form, "type_form": type_form}
    return render(request, 'post_form.html', context)

def delete_post(request,post_id):
    post = Post.objects.get(id=post_id, user=request.user)
    type_delete = 1
    if request.method == 'POST':
        post.delete()
        return redirect('login:panel_admin')
    
    return render(request, 'delete.html', {'post': post, "type_delete": type_delete})

def update_post(request,post_id):
    post = Post.objects.get(id=post_id, user = request.user)
    form = PostForm(instance=post)
    update = 1
    type_form = 1
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance = post)
        form.save()
        return redirect('login:panel_admin')

    context = {"form":form, "update":update, "type_form": type_form}
    return render(request,'post_form.html', context)

def create_document(request):
    form = DocumentForm()
    type_form = 2
    extension = None
    
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            new_document = form.save(commit=False)
            new_document.user = request.user
            consejo = Consejos.objects.get(user=request.user)
            new_document.consejo = consejo
            new_document.save()
            return redirect('login:panel_admin')
        
    extension = os.path.splitext(str(request.FILES.get('pdf')))[1]
    
    context = {"form":form, "type_form": type_form, "extension": extension}
    return render(request, 'post_form.html', context)

def delete_document(request,documents_id):
    document = Documents.objects.get(id=documents_id, user=request.user)
    type_delete = 2
    if request.method == 'POST':
        document.delete()
        return redirect('login:panel_admin')
    
    return render(request, 'delete.html', {'document': document, "type_delete": type_delete})

def create_banner(request):
    form = BannerForm()
    type_form = 3
    quantity_banners = Banner.objects.filter(user=request.user).count()
    message = ""
    
    if quantity_banners == 1:
        message = "Solamente puede añadir un Banner"
        context = {"form":form, "type_form": type_form, "message": message}
        return render(request, 'post_form.html', context)
    
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES)
        if form.is_valid():
            new_banner = form.save(commit=False)
            new_banner.user = request.user
            consejo = Consejos.objects.get(user=request.user)
            new_banner.consejo = consejo
            new_banner.save()
            return redirect('login:panel_admin')
            
    context = {"form":form, "type_form": type_form, "message": message}
    return render(request, 'post_form.html', context)


def delete_banner(request,banner_id):
    banner = Banner.objects.get(id=banner_id, user=request.user)
    type_delete = 3
    if request.method == 'POST':
        banner.delete()
        return redirect('login:panel_admin')
    
    return render(request, 'delete.html', {'banner': banner, "type_delete": type_delete})

def create_about(request):
    form = AboutUsForm()
    type_form = 4
    quantity_about = Aboutus.objects.filter(user=request.user).count()
    message = ""

    if quantity_about == 1:
        message = "Solamente puede añadir una descripción del consejo"
        context = {"form":form, "type_form": type_form, "message": message}
        return render(request, 'post_form.html', context)
    
    if request.method == 'POST':
        form = AboutUsForm(request.POST, request.FILES)
        if form.is_valid():
            new_about = form.save(commit=False)
            new_about.user = request.user
            consejo = Consejos.objects.get(user=request.user)
            new_about.consejo = consejo
            new_about.save()
            return redirect('login:panel_admin')
        
    context = {"form":form, "type_form": type_form}
    return render(request, 'post_form.html', context)

def update_about(request,aboutus_id):
    about = Aboutus.objects.get(id=aboutus_id, user = request.user)
    form = AboutUsForm(instance=about)
    update = 4
    type_form = 4
    
    if request.method == 'POST':
        form = AboutUsForm(request.POST, request.FILES, instance = about)
        form.save()
        return redirect('login:panel_admin')

    context = {"form":form, "update": update, "type_form": type_form}
    return render(request,'post_form.html', context)

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o Contraseña es incorrecto'
            })
        else:
            login(request, user)
            return redirect('login:panel_admin')

def signout(request):
    logout(request)
    return redirect('home')

def create_collaborator(request):
    form = CollaboratorForm()
    type_form = 5
    if request.method == 'POST':
        form = CollaboratorForm(request.POST, request.FILES)
        if form.is_valid():
            new_collaborator = form.save(commit=False)
            new_collaborator.user = request.user
            consejo = Consejos.objects.get(user=request.user)
            new_collaborator.consejo = consejo
            new_collaborator.save()
            return redirect('login:panel_admin')
        
    context={'form':form, "type_form": type_form}
    return render(request, 'post_form.html', context)


def delete_collaborator(request,collaborators_id):
    collaborator = Collaborators.objects.get(id=collaborators_id, user=request.user)
    type_delete = 5
    if request.method == 'POST':
        collaborator.delete()
        return redirect('login:panel_admin')
    
    return render(request, 'delete.html', {'collaborator': collaborator, "type_delete": type_delete})


def update_collaborator(request,collaborators_id):
    collaborator = Collaborators.objects.get(id=collaborators_id, user = request.user)
    form = CollaboratorForm(instance=collaborator)
    update = 5
    type_form = 5
    
    if request.method == 'POST':
        form = CollaboratorForm(request.POST, request.FILES, instance = collaborator)
        form.save()
        return redirect('login:panel_admin')

    context = {"form":form, "update":update, "type_form": type_form}
    return render(request,'post_form.html', context)


    

