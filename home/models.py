from django.db import models
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User
import datetime

class Consejos(models.Model):
    CONSEJO_CHOICES = [
        ('Local', 'Consejo Local'),
        ('Curul', 'Curul Especial'),
    ]
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150, blank=True)
    logo = ImageField(upload_to="consejos/logos")
    description = models.TextField(max_length=500, blank=True)
    type_consejo = models.CharField(max_length=5, choices= CONSEJO_CHOICES)
    user = models.ForeignKey(User, on_delete=models.PROTECT, default="")

    def __str__(self):
        return self.name

class Banner(models.Model):
    image = ImageField(upload_to="consejos/banners")
    consejo = models.ForeignKey(Consejos,null=True,blank= True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT, default="")

class Aboutus(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True)
    image = ImageField(upload_to="consejos/aboutus")
    consejo = models.ForeignKey(Consejos,null=True,blank= True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT, default="")

class Collaborators (models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    position = models.CharField(max_length=50)
    description = models.TextField(max_length=100, blank=True)
    image = ImageField(upload_to="consejos/collaborators")
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    consejo = models.ForeignKey(Consejos,null=True,blank= True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT, default="")

class Documents (models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to="consejos/documents")
    description = models.TextField(max_length=500, blank=True)
    date = models.DateTimeField()
    consejo = models.ForeignKey(Consejos,null=True,blank= True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT, default="")

    def save (self, *args, **kwargs):
        if not self .id:
            self.date = datetime.datetime.now()
            return super(Documents, self).save(*args, **kwargs)
        
