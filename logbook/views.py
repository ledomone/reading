from django.shortcuts import render
from .models import Book

# Create your views here.
from django.views.generic import TemplateView, ListView


class MainPageView(TemplateView):
    template_name = 'index.html'


index_view = MainPageView.as_view()


class BookListView(ListView):
    model = Book

