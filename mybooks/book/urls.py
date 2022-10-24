from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *

app_name = 'profile'
urlpatterns = [
    path('', BookListView.as_view(), name='profile'),
    path('add_book/', AddBookView.as_view(), name='add_book'),
    path('update_book/<int:book_id>', UpdateBookView.as_view(), name='update_book'),
    path('book/<int:book_id>/', BookDetailView.as_view(), name='book'),
    path("search/", Search.as_view(), name='search'),

    path('favorite/', FavoriteBookListView.as_view(), name="favorite_books"),
    path('names/', OrderBooksByName.as_view(), name='order_by_title'),
    path('rating/', OrderBooksByRating.as_view(), name='order_by_rating')
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)