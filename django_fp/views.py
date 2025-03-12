from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from final_project.models import ItemType, Genre, Item, Review
from final_project.forms import ItemForm

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

"""
Questions to ask:
    - Why charfields from models are not showing up? Despite seeming I've
        set everything up correctly
"""


def home(request):
    return render(request, 'final_project/home.html')

def films_serials(request):
    return render(request, 'final_project/films_serials.html')

def actors(request):
    return render(request, 'final_project/actors.html')

def detail(request, number):
    return render(request, 'final_project/detail.html', {'number': number})

def final_project_new(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('/final_project/films')
    else:
        form = ItemForm()

    return render(request, 'final_project/new.html', {'form': form})