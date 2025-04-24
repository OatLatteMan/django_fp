from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
# from django.utils import timezone
from datetime import date

User = get_user_model()


class ItemQuerySet(models.QuerySet):
    def top_rated(self):
        return self.filter(average_rating__gte=7.0)

    def with_reviews(self):
        return self.annotate(review_count=models.Count('reviews')).filter(review_count__gt=0)

    def films_only(self):
        return self.filter(type=ItemType.MOVIE)

class ActorQuerySet(models.QuerySet):
    def born_before(self, year):
        return self.filter(born__lt=date(year, 1, 1))

    def with_image(self):
        return self.exclude(image='actor/Matthew_McConaughey_X6VKhkL.jpg')

    def popular(self):
        return self.annotate(num_films=models.Count('films')).order_by('-num_films')


class ItemManager(models.Manager):
    def get_queryset(self):
        return ItemQuerySet(self.model, using=self.db)

    # Optional: custom methods are being exposed directly from manager
    def top_rated(self):
        return self.get_queryset().top_rated()

    def with_reviews(self):
        return self.get_queryset().with_reviews()

    def films_only(self):
        return self.get_queryset().films_only()

class ActorManager(models.Manager):
    def get_queryset(self):
        return ActorQuerySet(self.model, using=self.db)

    def born_before(self, year):
        return self.get_queryset().born_before(year)

    def with_image(self):
        return self.get_queryset().with_image()

    def popular(self):
        return self.get_queryset().popular()


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
    actors = models.ManyToManyField('Actor', related_name='films')
    name = models.CharField(max_length=40)
    title = models.CharField(max_length=50)
    desc = models.TextField(max_length=1000)
    type = models.IntegerField(choices=ItemType)
    genre = models.IntegerField(choices=Genre)
    review = models.ForeignKey(Review, blank=True, null=True, on_delete=models.SET_NULL, related_name='item_reviews')
    image = models.ImageField(blank=True, null=True, upload_to='item/')
    average_rating = models.FloatField(default=0.0)
    objects = ItemManager()
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("django_fp:item_detail", kwargs={"pk": self.pk})

class Actor(models.Model):
    name = models.CharField(max_length=40)
    born = models.DateField()
    image = models.ImageField(blank=True, null=True, upload_to='actor/')
    objects = ActorManager()

    def get_absolute_url(self):
        return reverse("django_fp:actor_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name

