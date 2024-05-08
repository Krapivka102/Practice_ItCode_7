from django.http import HttpResponse
from django.shortcuts import render
from . import models

def index(request):
    book = models.Book.objects.all()
    genre = models.Genre.objects.all()

    context = {'book': book,
               'genre': genre,
               'title': 'Список жанров',
    }

    return render(request, template_name='library/index.html', context=context)


def get_genre(request, genre_id):
    book = models.Book.objects.filter(genre=genre_id)
    genre = models.Genre.objects.all()
    gen = models.Genre.objects.get(pk=genre_id)

    context = {'book': book,
               'genre': genre,
               'gen': gen,
               }

    return render(request, template_name='library/genre.html', context=context)


def book_detail(request, pk):
    book = models.Book.objects.get(pk=pk)
    context = {'book': book}

    # Отображаем шаблон с информацией о книге
    return render(request, template_name='library/book_detail.html', context=context)