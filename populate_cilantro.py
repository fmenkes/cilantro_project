import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cilantro_project.settings')

import django

django.setup()

from cilantro.models import Category, Recipe, RecipeIngredient, Ingredient


def populate():
    mains_cat = add_cat("Mains")

    pasta = add_recipe(mains_cat, "Pasta Arrabiata", "Boil the Pasta")

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


def add_recipe(cat, name, instr):
    r = Recipe.objects.get_or_create(category=cat, name=name, instructions=instr)[0]
    return r


def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c


def add_ingr(recipe, name, amount):
    t = RecipeIngredient.objects.get_or_create(recipe=recipe, name=name, amount=amount)[0]
    return t


def populate_ingredients():
    for i in RecipeIngredient.objects.all():
        ing, created = Ingredient.objects.get_or_create(name=i.name.lower())
        if created:
            print "Ingredient %s created" % str(ing.name)
        else:
            print "Ingredient %s found!" % str(ing.name)

# Start execution here!
if __name__ == '__main__':
    print "Starting Cilantro population script..."
    populate()