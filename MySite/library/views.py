from django.http import HttpResponse
from django.shortcuts import render
from . import models

def index(request):
    book = models.Book.objects.all()

    return render(request, 'library/index.html', {'book': book, 'title': 'Список книг'})
