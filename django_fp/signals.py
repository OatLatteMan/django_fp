from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django_fp.models import User, Profile, Review
from django_fp.services import update_item_average_rating


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()

@receiver(post_save, sender=Review)
def review_saved(sender, instance, **kwargs):
    update_item_average_rating(instance.item)

@receiver(post_delete, sender=Review)
def review_deleted(sender, instance, **kwargs):
    update_item_average_rating(instance.item)

