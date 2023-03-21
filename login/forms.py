from django.forms import ModelForm
from .models import Post
from home.models import Documents, Banner, Aboutus

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'text']

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
