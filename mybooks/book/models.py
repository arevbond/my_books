from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse

# from mybooks.users.models import User
User = get_user_model()


class Category(models.TextChoices):
    artistic = 'artistic', 'Художественная литература'
    non_artistic = 'non_artistic', 'Не художественная литература'


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    title = models.CharField(max_length=255, verbose_name='Название книги')
    author = models.CharField(max_length=100, verbose_name='Автор книги')
    category = models.CharField(max_length=50, choices=Category.choices, verbose_name='Категория')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Обложка', blank=True, null=True)
    review = models.TextField(verbose_name='Рецензия')
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
                               verbose_name='Оценка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создание')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    favorite = models.BooleanField(default=False, verbose_name='Любимая книга')

    def __str__(self):
        return f'{self.user} - {self.title}'

    def get_absolute_url(self):
        return reverse('profile:book', kwargs={'book_id': self.pk})

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'