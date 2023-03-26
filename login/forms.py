from django import forms
from django.forms import ModelForm
from .models import Post
from home.models import Documents, Banner, Aboutus, Collaborators

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'subtitle','text']

class DocumentForm(ModelForm):
    class Meta:
        model = Documents
        fields = ['title', 'pdf', 'description']

class BannerForm(ModelForm):
    class Meta:
        model = Banner
        fields = ['image']

class AboutUsForm(ModelForm):
    class Meta:
        model = Aboutus
        fields = ['name', 'description', 'image']

class CollaboratorForm(ModelForm):
    class Meta:
        model = Collaborators
        fields = ['firstname', 'lastname', 'position', 'description', 'image', 'facebook', 'instagram', 'twitter']
