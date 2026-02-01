from django.db import models
from datetime import date

class Home(models.Model):
    heading = models.CharField(max_length=65)
    description = models.CharField(max_length=300)

class Diary(models.Model):
    title = models.CharField(max_length=65)
    created = models.DateField(default=date.today)
    content = models.CharField()


