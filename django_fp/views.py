from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django_fp import models
from django_fp.models import ItemType, Genre, Item, Review
from django_fp.forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

"""
Tabs:
    - Home (about)
    - Films and serials (detail)
    - Actors

Films:
    - Inception
    - Interstellar
    - 50 shades of gray

Serials:
    - Friends
    - Gotham
    - The Witcher
"""


def home(request):
    return render(request, 'django_fp/home.html')

# def list(request):
#     films = models.Item.objects.all()
#     return render(request, 'django_fp/films_list.html', {'films': films})

class ItemDetail(DetailView):
    model = models.Item

class ItemList(ListView):
    model = models.Item
    queryset = models.Item.objects.all()

    # paginate_by = 10

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     paginator = context['paginator']
    #     page_obj = context['page_obj']
    #     context['paginator_range'] = paginator.get_elided_page_range(
    #         page_obj.number,
    #         on_ends=1,
    #         on_each_side=1
    #     )
    #     return context

def actors(request):
    return render(request, 'django_fp/actors.html')

# def detail(request, pk):
#     film = get_object_or_404(models.Item, pk=pk)
#     return render(request, 'django_fp/item_detail.html', {'film': film})

def django_fp_new(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('/django_fp/films')
    else:
        form = ItemForm()

    return render(request, 'django_fp/new.html', {'form': form})