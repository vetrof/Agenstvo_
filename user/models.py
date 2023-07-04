from django.db import models

class Users(models.Model):
    email = models.EmailField(blank=True)
