from django.db import models

class Channel(models.Model):
    title = models.CharField(max_length=255)
    language = models.CharField(max_length=2)
    poster_image = models.URLField(max_length=255)
    description = models.TextField()
    maturity_rating = models.CharField(max_length=255)
    spoken_lang = models.CharField(max_length=255)
    caption_lang = models.CharField(max_length=255)

class Movie(Channel):
    duration = models.PositiveIntegerField()
    genre = models.CharField(max_length=255)
    

class TVShow(Channel):
    num_seasons = models.PositiveIntegerField()
    
class Season(models.Model):
    number = models.PositiveIntegerField()
    tvshow = models.ForeignKey(TVShow, on_delete=models.CASCADE)

class Episode(models.Model):
    number = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)