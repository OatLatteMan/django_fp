from django.shortcuts import render, redirect, get_object_or_404
from django_fp import models
from django_fp.models import Item, Actor
from django_fp.forms import ItemForm, ActorForm
from django_fp.forms import ReviewForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import UpdateView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms


def logout_view(request):
    logout(request)
    return render(request, 'django_fp/index.html')

def index(request):
    print(f"Logged-in user is: {request.user.id}")
    return render(request, 'django_fp/index.html')

class ItemUpdate(UpdateView):
    model = models.Item
    fields = ['name', 'desc', 'title', 'actors', 'type', 'genre', 'image']

    def get_success_url(self):
        return reverse_lazy('django_fp:item_detail', kwargs={'pk': self.object.pk})

class ItemUpdate(UpdateView):
    model = models.Item
    fields = ['name', 'desc', 'title', 'actors', 'type', 'genre', 'image']

    def get_success_url(self):
        return reverse_lazy('django_fp:item_detail', kwargs={'pk': self.object.pk})

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

class ItemList(LoginRequiredMixin, ListView):
    model = models.Item
    queryset = models.Item.objects.all()

    def get_login_url(self):
        return reverse_lazy('django_fp:index')

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Item.objects.all()
        else:
            return Item.objects.none()

class ActorDetail(DetailView):
    model = models.Actor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['films'] = self.object.films_actors.all()
        return context

class ActorList(LoginRequiredMixin, ListView):
    model = models.Actor
    queryset = models.Actor.objects.all()

    def get_login_url(self):
        return reverse_lazy('django_fp:index')

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Actor.objects.all()
        else:
            return Actor.objects.none()

def django_fp_new_film(request):
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

    return render(request, 'django_fp/new_film.html', {'form': form})

def django_fp_new_actor(request):
    if request.method == 'POST':
        form = ActorForm(request.POST, request.FILES)

        if form.is_valid():
            actor = form.save()
            actor.save()
            form.save_m2m()
            return redirect('/django_fp/actors')
    else:
        form = ActorForm()

    return render(request, 'django_fp/new_actor.html', {'form': form})

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
                return redirect('/django_fp/actors')

    return redirect('/django_fp/films')

def django_fp_delete_actor(request, number):
    if request.method == 'POST':
        if request.user.is_authenticated:
            try:
                print(f"Logged-in user is: {request.user.id}")
                actor = get_object_or_404(Actor, id=number)
                print(f"Actor found: {actor}")
                actor.delete()
                return redirect('/django_fp/actors/')
            except:
                return redirect('/django_fp/')

    return redirect('/django_fp/')

