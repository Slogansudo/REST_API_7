from django.db import models
from .hepsl import SaveImage


class Artist(models.Model):
    name = models.CharField(max_length=50)
    image = models.URLField()
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)


class Album(models.Model):
    title = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True, blank=True)
    cover = models.URLField()
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)


class Songs(models.Model):
    title = models.CharField(max_length=100)
    cover = models.URLField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
