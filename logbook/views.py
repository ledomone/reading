from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView
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