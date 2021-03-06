from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView
from django.db.models import Sum
from .models import Book
from .forms import BookCreateForm


class MainPageView(TemplateView):
    template_name = 'index.html'


index_view = MainPageView.as_view()


class BookListView(ListView):
    model = Book

    def get_queryset(self):
        qs = super(BookListView, self).get_queryset()
        return qs.filter(who=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['total'] = Book.objects.filter(who=self.request.user).aggregate(sum=Sum('pages'))
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(BookListView, self).dispatch(request, args, kwargs)


class BookView(DetailView):
    model = Book
    template_name = 'logbook/book_detail.html'

    def get_queryset(self):
        qs = super(BookView, self).get_queryset()
        return qs.filter(who=self.request.user)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(BookView, self).dispatch(request, args, kwargs)


class BookCreate(CreateView):
    model = Book
    template_name_suffix = '_create_form'
    fields = ['title', 'author', 'pages', 'date']
    form_class = BookCreateForm

    def get_success_url(self):
        return reverse('logbook:book-list')

    def form_valid(self, form):
        form.instance.who = self.request.user
        return super(BookCreate, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(BookCreate, self).dispatch(request, args, kwargs)


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('logbook:book-list')

    def get_queryset(self):
        qs = super(BookDelete, self).get_queryset()
        return qs.filter(who=self.request.user)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(BookDelete, self).dispatch(request, args, kwargs)