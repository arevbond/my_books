from .models import *

class BookMixinData:
    model = Book
    context_object_name = 'books'
    template_name = 'book/profile.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['story'] = 'История записей -'
        context['amout_books'] = Book.objects.filter(user=self.request.user).count()
        return context


class OtherBookMixinData:
    model = Book
    context_object_name = 'books'
    template_name = 'book/other_user_profile.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['story'] = 'История записей -'
        context['amout_books'] = Book.objects.filter(user_id=self.kwargs['user_id']).count()
        return context