from django import forms
from django.forms import ModelForm
from django_fp.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'desc', 'actors', 'title']
        widgets = {
            'name': forms.Textarea(attrs={'rows': 1}),
            'desc': forms.Textarea(attrs={'rows': 2}),
            'actors': forms.SelectMultiple(),
            'title': forms.Textarea(attrs={'rows': 1}),
        }