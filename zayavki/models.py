from django.db import models


class Zayavka(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    question = models.TextField()
    manager_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

