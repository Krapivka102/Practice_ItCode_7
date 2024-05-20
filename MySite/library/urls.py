from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('genre/<int:pk>', GenreView.as_view(), name='genre'),
    path('books/', BookList.as_view(), name='genre'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail')
]