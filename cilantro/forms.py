from django import forms
from cilantro.models import Category, Recipe, RecipeIngredient


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Name: ")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)


class RecipeForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Name:")
    servings = forms.CharField(max_length=40, help_text="Servings:", required=False)
    instructions = forms.CharField(max_length=1000, help_text="Instructions: ")
    slug = forms.SlugField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Recipe
        exclude = ('slug', 'category')


class RecipeIngredientForm(forms.ModelForm):
    name = forms.CharField(max_length=128)
    amount = forms.CharField(max_length=40, required=False)

    class Meta:
        model = RecipeIngredient
        fields = ('name', 'amount')