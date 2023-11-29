# myapp/models.py
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
    published_date = models.DateField()

    def __str__(self):
        return self.title

    def display_info(self):
        return f"{self.title} (Published on {self.published_date})"
