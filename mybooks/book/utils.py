from .models import *

class BookMixinData:
    model = Book
    context_object_name = 'books'
    template_name = 'book/profile.html'