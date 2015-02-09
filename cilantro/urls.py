from django.conf.urls import patterns, url

from cilantro import views

# TODO: Special-case the category 'Shopping Lists'
urlpatterns = patterns('',
                url(r'^$', views.index, name="index"),
                url(r'^evernote/$', views.evernote, name="evernote"),
                url(r'^evernote/send/$', views.send_recipe_to_evernote, name="send_recipe_to_evernote"),
                url(r'^add_category/$', views.add_category, name="add_category"),
                url(r'^delete_recipe/$', views.delete_recipe, name="delete_recipe"),
                url(r'^shopping_list/$', views.shopping_list, name="shopping_list"),
                url(r'^add_to_shopping_list/$', views.add_to_shopping_list, name="add_to_shopping_list"),
                url(r'^clear_shopping_list/$', views.clear_shopping_list, name="clear_shopping_list"),
                url(r'^(?P<category_name_slug>[\w\-]+)/add_recipe/$', views.add_recipe, name="add_recipe"),
                url(r'^(?P<category_name_slug>[\w\-]+)/$', views.category, name="category"),
                url(r'^(?P<category_name_slug>[\w\-]+)/(?P<recipe_name_slug>[\w\-]+)/$', views.recipe, name="recipe"),
)