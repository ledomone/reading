from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView
from .models import Book


class MainPageView(TemplateView):
    template_name = 'index.html'


index_view = MainPageView.as_view()


class BookListView(ListView):
    model = Book

    def get_queryset(self):
        qs = super(BookListView, self).get_queryset()
        return qs.filter(who=self.request.user.id)


class BookView(DetailView):
    model = Book
    template_name = 'logbook/book_detail.html'


class BookCreate(CreateView):
    model = Book
    template_name_suffix = '_create_form'
    fields = ['title', 'author', 'pages', 'date', 'who']
    # success_url = '/books'

    def get_success_url(self):
        return reverse('logbook:book-list')


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('logbook:book-list')