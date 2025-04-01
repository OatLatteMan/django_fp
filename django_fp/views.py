from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django_fp import models
from django_fp.models import ItemType, Genre, Item, Review
from django_fp.forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


def home(request):
    return render(request, 'django_fp/home.html')

class ItemDetail(DetailView):
    model = models.Item

class ItemList(ListView):
    model = models.Item
    queryset = models.Item.objects.all()

class ActorDetail(DetailView):
    model = models.Actor

class ActorList(ListView):
    model = models.Actor
    queryset = models.Actor.objects.all()

def django_fp_new(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('/django_fp/films')
    else:
        form = ItemForm()

    return render(request, 'django_fp/new.html', {'form': form})

def django_fp_delete_item(request, number):
    

