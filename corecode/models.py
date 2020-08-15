from django.db import models


# Create your models here.


class Subject(models.Model):
    """ Subject """
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
