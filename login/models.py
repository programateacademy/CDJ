from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from home.models import Consejos
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=50)
    image = models.FileField(upload_to="consejos/post/")
    subtitle = models.TextField(max_length=75, null=True)
    text = RichTextUploadingField()
    consejo = models.ForeignKey(Consejos,null=True,blank= True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT, default="")

    def __str__(self):
        return self.title

