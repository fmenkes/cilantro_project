import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cilantro_project.settings')

import django

django.setup()

from cilantro.models import Category, Recipe, Ingredient


def populate():
    mains_cat = add_cat("Mains")

    pasta = add_recipe(mains_cat, "Pasta Arrabiata", "Boil the Pasta")

    add_ingr(recipe=pasta, name="Garlic", amount="4 cloves")
    add_ingr(recipe=pasta, name="Pasta", amount="250g")
    add_ingr(recipe=pasta, name="Tomato", amount="400g")
    add_ingr(recipe=pasta, name="Chilies", amount="4")

    # Print out what we have added to the user.
    for c in Category.objects.all():
        for r in Recipe.objects.filter(category=c):
            for t in Ingredient.objects.filter(recipe=r):
                print "- {0} - {1} - {2}".format(str(c), str(r), str(t))


def add_recipe(cat, name, instr):
    r = Recipe.objects.get_or_create(category=cat, name=name, instructions=instr)[0]
    return r


def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c


def add_ingr(recipe, name, amount):
    t = Ingredient.objects.get_or_create(recipe=recipe, name=name, amount=amount)[0]
    return t

# Start execution here!
if __name__ == '__main__':
    print "Starting Cilantro population script..."
    populate()