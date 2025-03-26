from django import forms
from django.forms import ModelForm
from django_fp.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'desc']
        widgets = {
            'name': forms.Textarea(attrs={'rows': 1}),
            'desc': forms.Textarea(attrs={'rows': 4})
        }