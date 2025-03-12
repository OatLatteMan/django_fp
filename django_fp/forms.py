from django import forms
from django.forms import ModelForm
from final_project.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'desc']
        widgets = {
            'name': forms.Textarea(attrs={'rows': 2}),
            'desc': forms.Textarea(attrs={'rows': 4})
        }