from django.db import models
from django.conf import settings


class Book(models.Model):
    """
    One log entry of readed book
    """
    author = models.CharField(max_length=150, null=True)
    title = models.CharField(max_length=250, null=True)
    date = models.DateField(null=True, help_text="Date of completion of reading")
    pages = models.IntegerField(null=True)
    who = models.ForeignKey(settings.AUTH_USER_MODEL)