from django import forms
from cilantro.models import Category


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Name: ")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)


class RecipeForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Name: ")
