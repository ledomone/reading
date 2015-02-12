from django.conf.urls import patterns, include, url

from logbook.views import BookListView, BookView

urlpatterns = patterns('',
    url(r'^$', BookListView.as_view(), name='book-list'),
    url(r'^/(?P<pk>\d+)/$', BookView.as_view(), name='book-detail'),
)