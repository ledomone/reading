from django.conf.urls import patterns, include, url

from .views import BookListView, BookView, BookCreate, BookDelete

urlpatterns = patterns('',
    url(r'^$', BookListView.as_view(), name='book-list'),
    url(r'^(?P<pk>\d+)/$', BookView.as_view(), name='book-detail'),
    url(r'^create/$', BookCreate.as_view(), name='book-add'),
    url(r'^(?P<pk>\d+)/delete/$', BookDelete.as_view(), name='book-del'),
)