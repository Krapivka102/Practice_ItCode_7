from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from . import models


class BookList(ListView):
    model = models.Book
    context_object_name = "book"
    template_name = 'library/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        genre = models.Genre.objects.all()

        context["title"] = 'Список жанров'
        context["genre"] = genre

        return context


class GenreView(DetailView):
    model = models.Genre
    context_object_name = "genre"
    template_name = 'library/genre.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        genre_id = self.kwargs['pk']
        book = models.Book.objects.filter(genre=genre_id)
        gen = models.Genre.objects.get(pk=genre_id)

        context['book'] = book
        context['gen'] = gen

        return context


class BookDetailView(DetailView):
    model = models.Book
    context_object_name = "book"
    template_name = 'library/book_detail.html'


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

