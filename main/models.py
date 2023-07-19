from django.db import models
import datetime

from django.urls import reverse


class Realty(models.Model):
    title = models.CharField(max_length=100)
    info = models.TextField()
    price = models.IntegerField()
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)
    person = models.ForeignKey('Manager', null=True, blank=True, on_delete=models.PROTECT)
    img = models.ImageField(upload_to='house_image', blank=True)
    email = models.EmailField('Users', blank=True)

    def get_absolute_url(self):
        return reverse('main:object_info', args=[self.id])


class Gallery(models.Model):
    image = models.ImageField(upload_to='house_image')
    realty = models.ForeignKey(Realty, on_delete=models.CASCADE, related_name='images')


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'


class Manager(models.Model):
    name = models.CharField(max_length=30)
    surname = models.TextField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    email = models.TextField(null=True, blank=True)
    img = models.ImageField(blank=True)

    def __str__(self):
        return self.name
