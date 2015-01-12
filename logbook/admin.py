from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    fields = ('title', 'author', 'pages', 'date')
    list_display = ('title', 'author')


admin.site.register(Book, BookAdmin)
