from django import forms
from django.forms import ModelForm
from django_fp import models
from django_fp.models import Actor, Profile, Item

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

    def clean_name(self):
        name = self.cleaned_data.get('name')
        banned_names = ['untitled']

        if name and name.lower().strip() in banned_names:
            raise forms.ValidationError("Film name cannot be 'Untitled'.")
        return name

class ActorForm(forms.ModelForm):
    films = forms.ModelMultipleChoiceField(
        queryset=Item.objects.all(),
        widget=forms.SelectMultiple(),
        required=False,
        label="Select Films/Serials"
    )

    class Meta:
        model = Actor
        fields = ['name', 'born', 'image', 'films']
        widgets = {
            'name': forms.TextInput(),
            'image': forms.ClearableFileInput(attrs={'multiple': False}),
            'born': forms.DateInput(),
        }

    def save(self, commit=True):
        actor = super().save(commit=False)
        actor.save()  # Save first to get an ID

        films = self.cleaned_data.get('films')
        if films:
            actor.films.set(films)

        return actor

class ReviewForm(ModelForm):
    class Meta:
        model = models.Review
        fields = ['text', 'rate']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'cols': 40, 'class': 'text'}),
            'rate': forms.Select(choices=[(i, i) for i in range(1, 11)], attrs={'class': 'rate'}),  # for 1-5 rating
        }

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio']

