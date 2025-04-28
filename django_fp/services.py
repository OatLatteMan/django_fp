from django.db.models import Avg

def update_item_average_rating(item):
    if not item:
        return
    reviews = item.reviews.all()
    avg_rating = reviews.aggregate(Avg('rate'))['rate__avg']
    item.average_rating = avg_rating if avg_rating is not None else 0
    item.save()