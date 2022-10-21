from django import forms

from .models import Book


class AddBookForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Book


class UpdateBookForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Book
