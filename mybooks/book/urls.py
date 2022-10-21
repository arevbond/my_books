from django.urls import path

from .views import *

app_name = 'profile'
urlpatterns = [
    path('', BookListView.as_view(), name='profile'),
    path('add_book/', AddBookView.as_view(), name='add_book'),
    # path('update_book/', UpdateBookView.as_view(), name='update_book'),
    path('book/<int:book_id>/', BookDetailView.as_view(), name='book')
]