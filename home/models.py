from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=200,null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    position = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(upload_to='users',null=True,blank=True)
    class Meta:
        db_table = 'auth_user'

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Menu(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    info = models.TextField()
    image = models.ImageField(upload_to="foods/")
    sale = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class Special(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=500)
    content = models.TextField()
    image = models.ImageField(upload_to="special/")

    def __str__(self):
        return self.name

class Chefs(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    instagram = models.URLField(max_length=200,null=True, blank=True)
    facebook = models.URLField(max_length=200,null=True, blank=True)
    telegram = models.URLField(max_length=100,null=True, blank=True)
    youtube = models.URLField(max_length=200,null=True, blank=True)

    def __str__(self):
        return self.name

class Events(models.Model):
    name = models.CharField(max_length=200)
    sale = models.IntegerField()
    info = models.TextField()
    image = models.ImageField(upload_to="events")

    def __str__(self):
        return self.name

class SayingAbout(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.content


class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery")
    date = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()