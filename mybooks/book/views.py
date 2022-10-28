from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from .forms import *
from .utils import BookMixinData

from .help_funcs.dowloand_photo import dowloand_photo
from .help_funcs.dowloan_book_description import dowloand_book_desc


class BookListView(LoginRequiredMixin, BookMixinData, ListView):
    login_url = '/users/login/'

    def get_queryset(self):
        return Book.objects.filter(user=self.request.user).order_by('-time_create')


class UpdateBookView(UpdateView):
    form_class = UpdateBookForm
    template_name = 'book/update_book.html'
    pk_url_kwarg = 'book_id'
    model = Book

    def get_object(self, queryset=None):
        return Book.objects.get(user=self.request.user, id=self.kwargs.get('book_id'))

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        form.save()
        return redirect(self.get_success_url())


class AddBookView(CreateView):
    form_class = AddBookForm
    template_name = 'book/add_book.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.photo = dowloand_photo(obj.title, obj.author)
        obj.description = dowloand_book_desc(obj.title, obj.author)
        obj.save()
        return redirect('profile:profile')


class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    pk_url_kwarg = 'book_id'


class Search(BookMixinData, ListView):

    def get_queryset(self):
        return Book.objects.filter(Q(title__icontains=self.request.GET.get('search'), user=self.request.user) | Q(
            author__icontains=self.request.GET.get('search'), user=self.request.user))


class FavoriteBookListView(BookMixinData, ListView):

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['story'] = 'Ваши любимые книги'
        return context

    def get_queryset(self):
        return Book.objects.filter(user=self.request.user).filter(favorite=True)


class OrderBooksByName(BookMixinData, ListView):
    def get_queryset(self):
        return Book.objects.filter(user=self.request.user).order_by('-title')


class OrderBooksByRating(BookMixinData, ListView):
    def get_queryset(self):
        return Book.objects.filter(user=self.request.user).order_by('-rating')


class OrderBooksByTimeCreate(BookMixinData, ListView):
    def get_queryset(self):
        return Book.objects.filter(user=self.request.user).order_by('time_create')


def delete_book(request, book_id):
    book_to_delete = Book.objects.get(id=book_id)
    book_to_delete.delete()
    return redirect('profile:profile')
