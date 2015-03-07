from django.utils.translation import ugettext_lazy as _
from django import forms
from .models import Book


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'date', 'pages')
        labels = {
            'title': _("Book's title"),
            'date': _("Date of completion of reading"),
        }
        help_texts = {
            'date': _("Beware of the date format!"),
            'pages': _("Number of pages")
        }
