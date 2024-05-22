from django.shortcuts import render
from django.views.generic import ListView, DetailView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from . import models, filters, serializers


class BookViewSet(ModelViewSet):
    queryset = models.Book.objects.all()
    filterset_class = filters.Book
    serializer_class = serializers.Book

class Book(APIView):
    def get(self, request):
        qs = models.Book.objects.all()
        serializer = serializers.Book(qs, many=True)

        return Response(data=serializer.data)


    def post(self, request):
        serializer = serializers.Book(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'message': 'Ok'})

class BookList(ListView):
    model = models.Book
    context_object_name = "book"
    template_name = 'library/index.html'


    def get_filters(self):
        return filters.Book(self.request.GET)


    def get_queryset(self):
        return self.get_filters().qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        genre = models.Genre.objects.all()

        context["title"] = 'Список жанров'
        context["filters"] = self.get_filters()

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






