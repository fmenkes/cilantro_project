from django.shortcuts import render
from cilantro.models import Recipe, Category, RecipeIngredient
from cilantro.forms import CategoryForm, RecipeForm, RecipeIngredientForm
from django.forms.formsets import formset_factory
import pdb


def index(request):
    return render(request, 'cilantro/index.html', {})


def recipe(request, category_name_slug, recipe_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        recipe = Recipe.objects.filter(category=category).get(slug=recipe_name_slug)
        context_dict['category'] = category
        context_dict['recipe'] = recipe
        context_dict['ingredients'] = RecipeIngredient.objects.filter(recipe=recipe)
    except Recipe.DoesNotExist or Category.DoesNotExist:
        context_dict['recipe_name'] = "Not Found"

    return render(request, 'cilantro/recipe.html', context_dict)


def category(request, category_name_slug):
    """obsolete?"""
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        recipes = Recipe.objects.filter(category=category)
        context_dict['category'] = category
        context_dict['category_name'] = category.name
        context_dict['category_name_slug'] = category_name_slug
        context_dict['recipes'] = recipes
    except Category.DoesNotExist:
        pass

    return render(request, 'cilantro/category.html', context_dict)


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return index(request)
        else:
            print form.errors
    else:
        form = CategoryForm()

    return render(request, 'cilantro/add_category.html', {'form': form})


def add_recipe(request):
    recipe_formset = formset_factory(RecipeIngredientForm, extra=10)
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST)
        ingredients_form = recipe_formset(request.POST)

        if recipe_form.is_valid():
            recipe_name = recipe_form.cleaned_data['name']

            if ingredients_form.is_valid():
                recipe_form.save(commit=True)

                for form in ingredients_form.forms:
                    #pdb.set_trace()
                    if form.cleaned_data:
                        form.instance.recipe = Recipe.objects.get(name=recipe_name)
                        form.save(commit=True)

                return index(request)
            else:
                print ingredients_form.errors
        else:
            print recipe_form.errors

    else:
        recipe_form = RecipeForm()
        ingredients_form = recipe_formset()

    return render(request, 'cilantro/add_recipe.html', {'form': recipe_form, 'formset': ingredients_form})