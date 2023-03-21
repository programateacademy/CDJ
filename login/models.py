from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from home.models import Consejos

class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to="consejos/post/")
    text = RichTextUploadingField(max_length=200)
    consejo = models.ForeignKey(Consejos,null=True,blank= True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
