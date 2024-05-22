from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from rest_framework.test import APIClient
from library import models


class Test(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.genre = models.Genre.objects.create(name="Фэнтези")
        self.book = models.Book.objects.create(
            title="Ведьмак 1",
            author="Сапковский",
            description="Некое описание книги",
            genre=self.genre,
            pages=120,
            price=300,
            photo=SimpleUploadedFile("media/example.jpg", b"file_content", content_type="image/jpeg")
        )

    def test_list(self):
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)

    def test_detail(self):
        response = self.client.get(f'/books/{self.book.id}/')
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        data = {
            "title": "Новая книга",
            "author": "Автор",
            "description": "Описание новой книги",
            "genre": self.genre.id,
            "pages": 150,
            "price": 400,
        }
        response = self.client.post('/books/', data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_update(self):

        new_data = {
            'title': "Ведьмак 2",
            'author': "Сапковский",
            'description': "Описание второй книги",
            'genre': self.genre.id,
            'pages': 150,
            'price': 350,
        }

        response = self.client.put(f'/books/{self.book.id}/', data=new_data)

        self.assertEqual(response.status_code, 200)


    def test_partial_update(self):
        partial_new_data = {
            'description': "Обновленное описание"
        }

        response = self.client.patch(f'/books/{self.book.id}/', data=partial_new_data)

        self.assertEqual(response.status_code, 200)


    def test_delete(self):
        response = self.client.delete(f'/books/{self.book.id}/')
        self.assertEqual(response.status_code, 204)



