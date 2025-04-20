from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to='avatars/')
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class ItemType(models.IntegerChoices):
    MOVIE = 1, 'Film'
    TV_SHOW = 2, 'Serial'
    OTHER = 3, 'Others'

class Genre(models.IntegerChoices):
    SCIFI = 1, 'Sci-fi'
    DRAMA = 2, 'Drama'
    COMERY = 3, 'Comedy'

class Review(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    item = models.ForeignKey('Item', null=True, on_delete=models.SET_NULL, related_name='reviews')
    text = models.CharField(max_length=500)
    rate = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.user.username

class Item(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    actors = models.ManyToManyField('Actor', blank=True, related_name='films_actors')
    name = models.CharField(max_length=40)
    title = models.CharField(max_length=50)
    desc = models.TextField(max_length=1000)
    type = models.IntegerField(choices=ItemType)
    genre = models.IntegerField(choices=Genre)
    review = models.ForeignKey(Review, blank=True, null=True, on_delete=models.SET_NULL, related_name='item_reviews')
    image = models.ImageField(blank=True, null=True, upload_to='item/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("django_fp:item_detail", kwargs={"pk": self.pk})

class Actor(models.Model):
    film = models.ForeignKey(Item, null=True, on_delete=models.SET_NULL, related_name='actor_film')
    name = models.CharField(max_length=40)
    born = models.DateField()
    image = models.ImageField(blank=True, null=True, upload_to='actor/')

    def get_absolute_url(self):
        return reverse("django_fp:actor_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name

