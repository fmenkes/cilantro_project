from django.shortcuts import render, redirect
from cilantro.models import Recipe, Category, RecipeIngredient
from cilantro.forms import CategoryForm, RecipeForm, RecipeIngredientForm
from django.forms.formsets import formset_factory
from django.shortcuts import HttpResponseRedirect
from evernote.api.client import EvernoteClient
import evernote.edam.type.ttypes as types
import pdb


def index(request):
    return render(request, 'cilantro/index.html', {})


def evernote(request):
    context_dict = {}
    dev_token = "***REMOVED***"
    client = EvernoteClient(token=dev_token)
    user_store = client.get_user_store()
    user = user_store.getUser()
    context_dict['username'] = user.username

    return render(request, 'cilantro/evernote.html', context_dict)


def send_recipe_to_evernote(request):
    dev_token = "***REMOVED***"
    client = EvernoteClient(token=dev_token)
    note_store = client.get_note_store()
    note = types.Note()
    note.title = "I'm a test note!"
    note.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
    note.content += '<en-note>Hello, world! I was sent from %s.</en-note>' % request.get_full_path
    note_store.createNote(note)

    return render(request, 'cilantro/index.html')


def recipe(request, category_name_slug, recipe_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        recipe = Recipe.objects.filter(category=category).get(slug=recipe_name_slug)
        context_dict['category'] = category
        context_dict['recipe'] = recipe
        context_dict['ingredients'] = RecipeIngredient.objects.filter(recipe=recipe)
    except(Recipe.DoesNotExist, Category.DoesNotExist):
        context_dict['not_found'] = recipe_name_slug

    return render(request, 'cilantro/recipe.html', context_dict)


def category(request, category_name_slug):
    """No link to this view, but handy if someone navigates to the category by accident."""
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        recipes = Recipe.objects.filter(category=category)
        context_dict['category'] = category
        context_dict['category_name_slug'] = category_name_slug
        context_dict['recipes'] = recipes
    except Category.DoesNotExist:
        context_dict['not_found'] = category_name_slug

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


def add_recipe(request, category_name_slug):
    recipe_formset = formset_factory(RecipeIngredientForm, extra=10)
    cat = Category.objects.get(slug=category_name_slug)
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST)
        ingredients_form = recipe_formset(request.POST)

        if recipe_form.is_valid():
            recipe_form.instance.category = cat
            recipe_name = recipe_form.cleaned_data['name']

            if ingredients_form.is_valid():
                recipe_form.save(commit=True)

                for form in ingredients_form.forms:
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

    return render(request, 'cilantro/add_recipe.html', {'form': recipe_form,
                                                        'formset': ingredients_form,
                                                        'category': cat,
                                                        })


def delete_recipe(request):
    if request.method == 'GET':
        r_id = request.GET['recipe_id']
        Recipe.objects.filter(id=r_id).delete()
        print "Recipe %d deleted successfully." % int(r_id)

    # TODO: This doesn't seem to work for some reason?
    return render(request, 'cilantro/index.html', {})