from django.conf.urls import patterns, url

from cilantro import views

urlpatterns = patterns('',
                url(r'^$', views.index, name="index"),
                url(r'^add_category/$', views.add_category, name="add_category"),
                url(r'^(?P<category_name_slug>[\w\-]+)/$', views.category, name="category"),
                url(r'^(?P<category_name_slug>[\w\-]+)/(?P<recipe_name_slug>[\w\-]+)/$', views.recipe, name="recipe"),
)