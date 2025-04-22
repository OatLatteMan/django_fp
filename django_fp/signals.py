from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django_fp.models import User, Profile, Review, Item


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