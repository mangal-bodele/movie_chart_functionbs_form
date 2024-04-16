from django.db import models

class Moviechart(models.Model):

    movie = models.CharField(max_length=10)
    release_year = models.CharField(max_length=10)
    industry = models.CharField(max_length=20)
    language = models.CharField(max_length=10)


