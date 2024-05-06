from django.db import models


class User(models.Model):
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    patronynic = models.CharField('Отчество', max_length=100, blank=True)
    email = models.EmailField('Электронная почта', unique=True)
    phone = models.CharField('Телефон', max_length=20, blank=True, null=True)
    registration_date = models.DateField('Дата регистрации', auto_now_add=True)
    date_birth = models.DateField('День рождения')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    title = models.CharField('Название', max_length=200)
    author = models.CharField('Автор', max_length=100)
    description = models.TextField('Описание', blank=True)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, verbose_name='Жанр', null=True)
    public_date = models.DateField('Дата выпуска', blank=True, null=True)
    pages = models.PositiveIntegerField('Количество страниц', blank=True, null=True)
    price = models.DecimalField('Цена', max_digits=5, decimal_places=2)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото', blank=True, null=True)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField('Название жанра', max_length=100)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name