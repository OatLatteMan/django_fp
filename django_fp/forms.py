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

class ReviewForm(ModelForm):
    class Meta:
        model = models.Review
        fields = ['text', 'rate']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 2}),
            'rate': forms.Select()
        }