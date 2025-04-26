from .models import Item, Actor

def top_ranked_items_and_actors(request):
    top_items = Item.objects.order_by('-views')[:4]
    top_actors = Actor.objects.order_by('-views')[:4]
    return {
        'top_items': top_items,
        'top_actors': top_actors
    }

def search_suggestions(request):
    all_item_names = Item.objects.values_list('name', flat=True)
    all_actor_names = Actor.objects.values_list('name', flat=True)

    return {
        'all_item_names': all_item_names,
        'all_actor_names': all_actor_names,
    }

