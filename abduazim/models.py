from django.db import models
from ckeditor.fields import RichTextField

class About(models.Model):
    name = models.CharField(max_length=250)
    picture = models.ImageField(null=True, blank=True, upload_to=".")
    title = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone = models.IntegerField()
    birthday = models.DateField()
    location = models.CharField(max_length=250)
    about_me = RichTextField()

    def __str__(self) :
        return f"{self.name}{self.about_me}"

class Comment(models.Model):
    name = models.CharField(max_length=250)
    picture = models.ImageField(upload_to=".")
    comentary = models.TextField()

    def __str__(self):
        return self.name

class ClientLogo(models.Model):
    picture = models.ImageField(null=True, blank=True, upload_to=".")
    url = models.CharField(null=True, blank=True, max_length=250, default="#")

class Education(models.Model):
    name = models.CharField(max_length=250)
    date = models.DateField()
    text = RichTextField()

    def __str__(self):
        return f"{self.name} ::{self.text}"
    
class Experince(models.Model):
    name = models.CharField(max_length=250)
    position = models.CharField(max_length=500)
    date = models.CharField(max_length=250)
    text = RichTextField()

    def __str__(self):
        return f"{self.name} {self.position}"

class Category(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.name}"

class Portfolio(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    picture = models.ImageField(upload_to=".")
    link = models.CharField(null=True, blank=True, max_length=250, default="#")
    content = RichTextField()
    date = models.DateField(null=True, blank=True)

    
    def __str__(self):
        return f"{self.name} categry {self.category}"
    
class Skills(models.Model):
    name = models.CharField(max_length=500)
    lavel = models.IntegerField(default=50)

    def __str__(self):
        return f"{self.name} daraja {self.lavel}"


class Service(models.Model):
    name = models.CharField(max_length=250)
    picture = models.FileField(upload_to=".")
    text = models.TextField()

    def __str__(self):
        return f"{self.name} {self.text}"

class Blog(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=500)
    blog = RichTextField()
    shortblog = models.CharField(max_length=250)
    picture = models.ImageField(null=True, blank=True, upload_to=".")

    def __str__(self):
        return f"{self.title} {self.shortblog}"

