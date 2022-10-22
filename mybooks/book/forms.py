from django import forms

from .models import Book


class AddBookForm(forms.ModelForm):
    class Meta:
        fields = ('title', 'author', 'category', 'photo', 'review', 'rating', 'favorite')
        model = Book


class UpdateBookForm(forms.ModelForm):
    class Meta:
        fields = ('title', 'author', 'category', 'photo', 'review', 'rating', 'favorite')
        model = Book