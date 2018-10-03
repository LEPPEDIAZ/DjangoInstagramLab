from django.db import models
from django.contrib.auth import get_user_model

class USER(models.Model):
    title = models.CharField(max_length=30)
    

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class FOLLOW(models.Model):
    headline = models.CharField(max_length=100)
    USER = models.ManyToManyField(USER)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)

class POST(models.Model):
    title = models.CharField(max_length=30)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)

class LIKE(models.Model):
    headline = models.CharField(max_length=100)
    POST = models.ManyToManyField(POST)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)
class NOLIKE(models.Model):
    headline = models.CharField(max_length=100)
    POST = models.ManyToManyField(POST)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)

class Publicar(models.Model):
    headline = models.CharField(max_length=100)
    USER = models.ManyToManyField(USER)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)
# Create your models here.
