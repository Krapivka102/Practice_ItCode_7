from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('books', BookViewSet, basename='books')


urlpatterns = [
    path('api/', Book.as_view(), name='home'),
    path('genre/<int:pk>/', GenreView.as_view(), name='genre'),
    path('index/', BookList.as_view(), name='book_list'),
    path('book_detail/<int:pk>/', BookDetailView.as_view(), name='book_detail')
]

urlpatterns += router.urls