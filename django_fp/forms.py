from django import forms
from django.forms import ModelForm
from django_fp import models

class ItemForm(ModelForm):
    class Meta:
        model = models.Item
        fields = ['name', 'desc', 'actors', 'title', 'type', 'genre', 'image']
        widgets = {
            'name': forms.TextInput(),
            'desc': forms.Textarea(attrs={'rows': 2}),
            'actors': forms.SelectMultiple(choices=models.Actor),
            'title': forms.Textarea(attrs={'rows': 1}),
            'type': forms.Select(choices=models.ItemType),
            'genre': forms.Select(choices=models.Genre),
            'image': forms.ClearableFileInput(attrs={'multiple': False}),
        }