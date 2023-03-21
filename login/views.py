from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm, DocumentForm, BannerForm, AboutUsForm
from home.models import Documents, Banner, Aboutus
import os

def panel_admin(request):
    posts = Post.objects.all() 
    documents = Documents.objects.all()
    banners = Banner.objects.all()
    about = Aboutus.objects.all()
    context = {'posts':posts, 'documents': documents, 'banners': banners, 'aboutus': about}
    return render(request, 'panel_admin.html', context)

def create_post(request):
    form = PostForm()
    type_form = 1
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login:panel_admin')
        
    context={'form':form, "type_form": type_form}
    return render(request, 'post_form.html', context)

def delete_post(request,post_id):
    post = Post.objects.get(id=post_id)
    type_delete = 1
    if request.method == 'POST':
        post.delete()
        return redirect('login:panel_admin')
    
    return render(request, 'delete.html', {'post': post, "type_delete": type_delete})

def update_post(request,post_id):
    post = Post.objects.get(id=post_id)
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
            form.save()
            return redirect('login:panel_admin')
        
    extension = os.path.splitext(str(request.FILES.get('pdf')))[1]
    
    context = {"form":form, "type_form": type_form, "extension": extension}
    return render(request, 'post_form.html', context)

def delete_document(request,documents_id):
    document = Documents.objects.get(id=documents_id)
    type_delete = 2
    if request.method == 'POST':
        document.delete()
        return redirect('login:panel_admin')
    
    return render(request, 'delete.html', {'document': document, "type_delete": type_delete})

def create_banner(request):
    form = BannerForm()
    type_form = 4
    quantity_banners = Banner.objects.count()
    message = ""
    
    if quantity_banners == 1:
        message = "Solamente puede añadir un Banner"
        context = {"form":form, "type_form": type_form, "message": message}
        return render(request, 'post_form.html', context)
    
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login:panel_admin')
            
    context = {"form":form, "type_form": type_form, "message": message}
    return render(request, 'post_form.html', context)


def delete_banner(request,banner_id):
    banner = Banner.objects.get(id=banner_id)
    type_delete = 3
    if request.method == 'POST':
        banner.delete()
        return redirect('login:panel_admin')
    
    return render(request, 'delete.html', {'banner': banner, "type_delete": type_delete})

def create_about(request):
    form = AboutUsForm()
    type_form = 4
    
    if request.method == 'POST':
        form = AboutUsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login:panel_admin')
        
    context = {"form":form, "type_form": type_form}
    return render(request, 'post_form.html', context)

def update_about(request,aboutus_id):
    about = Aboutus.objects.get(id=aboutus_id)
    form = AboutUsForm(instance=about)
    update = 4
    type_form = 4
    
    if request.method == 'POST':
        form = AboutUsForm(request.POST, request.FILES, instance = about)
        form.save()
        return redirect('login:panel_admin')

    context = {"form":form, "update": update, "type_form": type_form}
    return render(request,'post_form.html', context)

    





    

