from django.db import models

class Home(models.Model):
    heading = models.CharField(max_length=65)
    description = models.TextField(max_length=300)

class Diary(models.Model):
    title = models.CharField(max_length=65)
    created = models.DateField(auto_now=True)
    content = models.TextField()


