from django import forms
from django.forms import ModelForm
from django_fp import models
from django.db import models as m

class ItemForm(ModelForm):
    class Meta:
        model = models.Item
        fields = ['name', 'desc', 'actors', 'title', 'type', 'genre', 'image']
        widgets = {
            'name': forms.TextInput(),
            'desc': forms.Textarea(attrs={'rows': 2}),
            'actors': forms.SelectMultiple(),
            'title': forms.Textarea(attrs={'rows': 1}),
            'type': forms.Select(choices=models.ItemType),
            'genre': forms.Select(choices=models.Genre),
            'image': forms.ClearableFileInput(upload_to='/item'),
        }