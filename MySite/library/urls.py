from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('genre/<int:genre_id>', get_genre, name='genre'),
    path('books/<int:pk>/', book_detail, name='book_detail')
]