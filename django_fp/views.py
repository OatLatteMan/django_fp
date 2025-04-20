from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django_fp import models
from django_fp.models import Item, Actor
from django_fp.forms import ItemForm, ActorForm, ReviewForm, ProfileForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import UpdateView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def profile_view(request):
    return render(request, 'profile.html', {'profile': request.user.profile})

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile_edit.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'django_fp/index.html')

def index(request):
    return render(request, 'django_fp/index.html')

class ItemUpdate(UpdateView):
    model = models.Item
    fields = ['name', 'desc', 'title', 'actors', 'type', 'genre', 'image']

    def get_success_url(self):
        return reverse_lazy('django_fp:item_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        response = super().form_valid(form)
        item = form.instance  # the updated object
        messages.success(self.request, f'🎬 Item "{item.name}" successfully updated.')
        return response

class ActorUpdate(UpdateView):
    model = models.Actor
    fields = ['name', 'born', 'film', 'image']

    def get_success_url(self):
        return reverse_lazy('django_fp:actor_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        response = super().form_valid(form)
        actor = form.instance
        messages.success(self.request, f'🎭 Actor "{actor.name}" successfully updated!')
        return response

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
    # context_object_name = 'actor'

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
            try:
                item = get_object_or_404(Item, id=number, user=request.user) #
                item.delete()
                messages.success(request, f'🎬 Item "{item.name}" successfully deleted.')  # ✅ SUCCESS MESSAGE
                return redirect('/django_fp/films/')
            except:
                messages.error(request, "Item not found or not owned by you.")  # ❌ ERROR MESSAGE
                return redirect('/django_fp/actors')

    return redirect('/django_fp/films')

def django_fp_delete_actor(request, number):
    if request.method == 'POST':
        if request.user.is_authenticated:
            try:
                actor = get_object_or_404(Actor, id=number)
                actor.delete()
                messages.success(request, f'🎭 Actor "{actor.name}" successfully deleted.')  # ✅ SUCCESS MESSAGE
                return redirect('/django_fp/actors/')
            except:
                messages.error(request, "Actor not found or not owned by you.")  # ❌ ERROR MESSAGE
                return redirect('/django_fp/')

    return redirect('/django_fp/')

