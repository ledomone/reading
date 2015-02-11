from django.conf.urls import patterns, include, url
from django.contrib import admin
from logbook.views import BookListView, BookView

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^books/$', BookListView.as_view(), name='book-list'),
    url(r'^books/(?P<pk>\d+)/$', BookView.as_view(), name='book-detail'),
    url(r'^$', 'logbook.views.index_view', name='main-page'),
    url(r'^accounts/', include('allauth.urls')),
)
