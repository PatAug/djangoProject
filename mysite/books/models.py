from django.db import models
from django.utils import timezone


# Create your models here.

class BookList(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    createdDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

