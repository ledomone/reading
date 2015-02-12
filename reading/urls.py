from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^books/', include('logbook.urls', namespace='logbook')),
    url(r'^$', 'logbook.views.index_view', name='main-page'),
    url(r'^accounts/', include('allauth.urls')),
)
