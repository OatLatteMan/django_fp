from django.core.management.base import BaseCommand
from django_fp.models import Review

class Command(BaseCommand):
    help = 'Deletes reviews that are not linked to any item.'

    def handle(self, *args, **kwargs):
        orphan_reviews = Review.objects.filter(item__isnull=True)
        count = orphan_reviews.count()

        if count == 0:
            self.stdout.write(self.style.SUCCESS('No orphan reviews found.'))
        else:
            orphan_reviews.delete()
            self.stdout.write(self.style.SUCCESS(f'Deleted {count} orphan review(s).'))