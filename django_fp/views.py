from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django_fp.models import ItemType, Genre, Item, Review
from django_fp.forms import ItemForm

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

def films_serials(request):
    return render(request, 'django_fp/films_serials.html')

def actors(request):
    return render(request, 'django_fp/actors.html')

def detail(request, number):
    return render(request, 'django_fp/detail.html', {'number': number})

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