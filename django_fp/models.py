from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class ItemType(models.IntegerChoices):
    MOVIE = 1, 'Film'
    TV_SHOW = 2, 'Seriál'
    OTHER = 3, 'Ostatní'

class Genre(models.IntegerChoices):
    SCIFI = 1, 'Sci-fi'
    DRAMA = 2, 'Drama'
    COMERY = 3, 'Komedie'

class Item(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    type = models.IntegerField(choices=ItemType)
    genre = models.IntegerField(choices=Genre)

    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    rate = models.PositiveSmallIntegerField()

