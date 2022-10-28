from django import forms
# from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE

from .models import Book


class AddBookForm(forms.ModelForm):
    # review = forms.CharField(label='Отзыв', widget=TinyMCE(attrs={'cols': 10, 'rows': 10}))

    class Meta:
        fields = ('title', 'author', 'category', 'review', 'rating', 'favorite')
        model = Book


class UpdateBookForm(forms.ModelForm):
    # review = forms.CharField(label='Отзыв', widget=TinyMCE(attrs={'cols': 10, 'rows': 10}))
    class Meta:
        fields = ('title', 'author', 'category', 'photo', 'review', 'rating', 'favorite')
        model = Book
