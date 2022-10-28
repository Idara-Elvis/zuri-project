from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Artiste(models.Models):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField(max_length=100)

    def __str__(self):
        return self.first_name + self.last_name


class Song(models.Model):
    title = models.CharField(max_length=200)
    date_released = models.DateField(auto_now_add=True)
    likes = models.IntegerField(max_length=1000000)
    artiste_id = models.ForeignKey(Artiste,on_delete=models.CASCADE, related_name="song")

    def __str__(self):
        return self.title



class Lyric(models.model):
    content = models.TextField(null=True, blank=True)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="lyric")

    def __str__(self):
        return self.content