from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import *


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'book/profile.html'

    login_url = '/users/login/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['amout_books'] = Book.objects.all().count()
        return context


class UpdateBookView(UpdateView):
    form_class = UpdateBookForm
    template_name = 'book/update_book.html'
    pk_url_kwarg = 'book_id'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return redirect('profile:profile')


class AddBookView(CreateView):
    form_class = AddBookForm
    template_name = 'book/add_book.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return redirect('profile:profile')


class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    context_object_name = 'book'
    pk_url_kwarg = 'book_id'
