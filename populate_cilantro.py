import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cilantro_project.settings')

import django

django.setup()

from cilantro.models import Category, Recipe, RecipeIngredient, Ingredient
from django.contrib.auth.models import User


def populate():
    admin = User.objects.get_by_natural_key("CilantroAdmin")

    mains_cat = add_cat("Mains", admin)
    cilantro_cat = add_cat("Shopping Lists", admin)

    pasta = add_recipe(mains_cat, admin, "Pasta Arrabiata", "Boil the Pasta")
    shoppinglist = create_shopping_list(cilantro_cat, admin)

    add_ingr(recipe=pasta, name="Garlic", amount="4 cloves")
    add_ingr(recipe=pasta, name="Pasta", amount="250g")
    add_ingr(recipe=pasta, name="Tomato", amount="400g")
    add_ingr(recipe=pasta, name="Chilies", amount="4")

    populate_ingredients()

    # Print out what we have added to the user.
    for c in Category.objects.all():
        for r in Recipe.objects.filter(category=c):
            for t in RecipeIngredient.objects.filter(recipe=r):
                print "- {0} - {1} - {2}".format(str(c), str(r), str(t))

    if shoppinglist:
        print "Shopping List created succesfully."


def add_recipe(cat, user, name, instr=""):
    r = Recipe.objects.get_or_create(category=cat, user=user, name=name, instructions=instr)[0]
    return r


def create_shopping_list(cat, admin):
    l = Recipe.objects.get_or_create(category=cat, user=admin, name="Shopping List", is_shopping_list=True)[0]
    return l


def add_cat(name, user):
    c = Category.objects.get_or_create(name=name, user=user)[0]
    return c


def add_ingr(recipe, name, amount):
    t = RecipeIngredient.objects.get_or_create(recipe=recipe, name=name, amount=amount)[0]
    return t


def populate_ingredients():
    for i in RecipeIngredient.objects.all():
        ing, created = Ingredient.objects.get_or_create(name=i.name.lower())
        if created:
            print "Ingredient %s created" % ing.name
        else:
            print "Ingredient %s found!" % ing.name

# Start execution here!
if __name__ == '__main__':
    print "Starting Cilantro population script..."
    populate()