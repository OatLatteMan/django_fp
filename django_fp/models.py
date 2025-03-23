from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse

User = get_user_model()

class ItemType(models.IntegerChoices):
    MOVIE = 1, 'Film'
    TV_SHOW = 2, 'Seriál'
    OTHER = 3, 'Ostatní'

    def __str__(self):
        return self.MOVIE, self.TV_SHOW, self.OTHER

class Genre(models.IntegerChoices):
    SCIFI = 1, 'Sci-fi'
    DRAMA = 2, 'Drama'
    COMERY = 3, 'Komedie'

class Item(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=1000)
    type = models.IntegerField(choices=ItemType)
    genre = models.IntegerField(choices=Genre)
    image = models.ImageField(blank=True, null=True, upload_to='item/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("django_fp:item_detail", kwargs={"pk": self.pk})

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    rate = models.PositiveSmallIntegerField()

