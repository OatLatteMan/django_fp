from django import forms
from django.forms import ModelForm
from django_fp import models

class ItemForm(ModelForm):
    class Meta:
        model = models.Item
        fields = ['name', 'desc', 'actors', 'title', 'type', 'genre', 'image', 'review']
        widgets = {
            'name': forms.TextInput(),
            'desc': forms.Textarea(attrs={'rows': 2}),
            'actors': forms.SelectMultiple(),
            'title': forms.Textarea(attrs={'rows': 1}),
            'type': forms.Select(choices=models.ItemType),
            'genre': forms.Select(choices=models.Genre),
            'image': forms.ClearableFileInput(attrs={'multiple': False}),
            'review': forms.Select()
        }

class ActorForm(ModelForm):
    class Meta:
        model = models.Actor
        fields = ['name', 'born', 'image', 'film']
        widgets = {
            'name': forms.TextInput(),
            'image': forms.ClearableFileInput(attrs={'multiple': False}),
            'born': forms.DateInput(),
            'film': forms.Select()
        }

    def save(self, commit=True):
        actor = super().save(commit=False)

        # Save the actor first if commit is True
        if commit:
            actor.save()

        # Now, associate this actor with the selected film
        film = self.cleaned_data['film']
        film.actors.add(actor)  # Add the actor to the film's actors

        return actor

class ReviewForm(ModelForm):
    class Meta:
        model = models.Review
        fields = ['text', 'rate']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'cols': 40, 'class': 'text'}),
            'rate': forms.Select(choices=[(i, i) for i in range(1, 11)], attrs={'class': 'rate'}),  # for 1-5 rating
        }