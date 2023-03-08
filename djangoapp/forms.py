from django import forms
from .models import Category , News
from django.forms import TextInput, Textarea

class NewsForm(forms.ModelForm):
    class Meta:
        model= News
        fields= ['title','content','is_bool','category']
        widgets={
            'title': TextInput(attrs={"class":"form-control"}),
            'content': Textarea(attrs={"class":"form-control"}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['title']
        
        widgets={
            'title':TextInput(attrs={'class':'form-control'})
        }
    

class SearchForm(forms.ModelForm):
    class Meta:
        model= News
        fields= ['title']
        widgets={
            'title': TextInput(attrs={"class":"form-control"}),
        }

