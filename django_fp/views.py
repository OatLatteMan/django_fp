from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django_fp import models
from django_fp.models import ItemType, Genre, Item, Review
from django_fp.forms import ItemForm
from django_fp.forms import ReviewForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import logout
from django.urls import reverse


def logout_view(request):
    logout(request)
    return render(request, 'django_fp/index.html')

def index(request):
    print(f"Logged-in user is: {request.user.id}")
    return render(request, 'django_fp/index.html')

class ItemDetail(DetailView):
    model = models.Item
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review_form'] = ReviewForm()
        context['reviews'] = self.object.reviews.all()

        return context

    def post(self, request, *args, **kwargs):
        item = self.get_object()

        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.user = request.user
            new_review.item = item
            new_review.save()
            return redirect(f'/django_fp/films/{item.pk}')

        return self.get(request, *args, **kwargs)

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
            item.user = request.user
            item.save()
            form.save_m2m()
            return redirect('/django_fp/films')
    else:
        form = ItemForm()

    return render(request, 'django_fp/new.html', {'form': form})

def django_fp_delete_item(request, number):
    if request.method == 'POST':
        if request.user.is_authenticated:
            print(f"Trying to delete item with id {number} for user {request.user.id}")
            try:
                print(f"Logged-in user is: {request.user.id}")
                item = get_object_or_404(Item, id=number, user=request.user) #
                print(f"Item found: {item}")
                item.delete()
                return redirect('/django_fp/films/')
            except:
                print("Item not found or does not belong to the user.")
                return redirect('/django_fp/')

    return redirect('/django_fp/')

