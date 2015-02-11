from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'cilantro.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^cilantro/', include('cilantro.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.backends.simple.urls')),
)
