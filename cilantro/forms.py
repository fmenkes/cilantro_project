from django import forms
from django.forms.models import modelformset_factory
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
        fields = ('name', 'servings', 'instructions')


class RecipeIngredientForm(forms.ModelForm):
    name = forms.CharField(max_length=128)
    amount = forms.CharField(max_length=40, required=False)

    class Meta:
        model = RecipeIngredient
        fields = ('name', 'amount')

ShoppingListFormSetBase = modelformset_factory(RecipeIngredient, extra=0, fields=('name', 'value', 'unit'))


class ShoppingListFormSet(ShoppingListFormSetBase):
    def add_fields(self, form, index):
        super(ShoppingListFormSet, self).add_fields(form, index)
        form.fields['is_checked'] = forms.BooleanField(required=False)