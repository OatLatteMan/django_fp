from .models import Item, Actor

def top_ranked_items_and_actors(request):
    top_items = Item.objects.order_by('-views')[:4]
    top_actors = Actor.objects.order_by('-views')[:4]
    return {
        'top_items': top_items,
        'top_actors': top_actors
    }
