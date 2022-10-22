from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from .models import *
from .forms import *
from .utils import BookMixinData


class BookListView(LoginRequiredMixin, BookMixinData, ListView):
    login_url = '/users/login/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['amout_books'] = Book.objects.all().count()
        return context


class UpdateBookView(UpdateView):
    form_class = UpdateBookForm
    template_name = 'book/update_book.html'
    pk_url_kwarg = 'book_id'

    def get_object(self, queryset=None):
        print(self.kwargs)
        return Book.objects.get(user=self.request.user, id=self.kwargs.get('book_id'))

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
    pk_url_kwarg = 'book_id'


class Search(BookMixinData, ListView):

    def get_queryset(self):
        return Book.objects.filter(Q(title__icontains=self.request.GET.get('search')) | Q(author__icontains=self.request.GET.get('search')))


class FavoriteBookListView(BookMixinData, ListView):

    def get_queryset(self):
        return Book.objects.filter(favorite=True)


class OrderBooksByName(BookMixinData, ListView):
    def get_queryset(self):
        return Book.objects.all().order_by('-title')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['amout_books'] = Book.objects.all().count()
        return context


class OrderBooksByRating(BookMixinData, ListView):
    def get_queryset(self):
        return Book.objects.all().order_by('-rating')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['amout_books'] = Book.objects.all().count()
        return context