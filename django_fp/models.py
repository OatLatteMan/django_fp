from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

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
    rate = models.PositiveSmallIntegerField(default=1)

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
    average_rating = models.FloatField(default=0.0)

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

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()

def update_item_average_rating(item):
    reviews = item.reviews.all()
    if reviews.exists():
        avg = sum([r.rate for r in reviews]) / reviews.count()
    else:
        avg = 0.0
    item.average_rating = avg
    item.save()

@receiver(post_save, sender=Review)
def recalculate_rating_on_save(sender, instance, **kwargs):
    update_item_average_rating(instance.item)

@receiver(post_delete, sender=Review)
def recalculate_rating_on_delete(sender, instance, **kwargs):
    update_item_average_rating(instance.item)

