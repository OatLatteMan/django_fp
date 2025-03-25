from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from datetime import date
from django.contrib import admin

User = get_user_model()

class ItemType(models.IntegerChoices):
    MOVIE = 1, 'Film'
    TV_SHOW = 2, 'Serial'
    OTHER = 3, 'Others'

class Genre(models.IntegerChoices):
    SCIFI = 1, 'Sci-fi'
    DRAMA = 2, 'Drama'
    COMERY = 3, 'Comedy'

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey('Item', on_delete=models.CASCADE, related_name='reviews')
    text = models.CharField(max_length=500)
    rate = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.user.username

class Item(models.Model):
    name = models.CharField(max_length=40)
    title = models.CharField(max_length=50)
    desc = models.TextField(max_length=1000)
    type = models.IntegerField(choices=ItemType)
    genre = models.IntegerField(choices=Genre)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='item_reviews')
    image = models.ImageField(blank=True, null=True, upload_to='item/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("django_fp:item_detail", kwargs={"pk": self.pk})

class Actor(models.Model):
    film = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='actor_film')
    name = models.CharField(max_length=40)
    born = models.DateField()

    def __str__(self):
        return self.name

