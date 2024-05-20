from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from library import models


class Test(TestCase):
    def setUp(self):
        self.client = Client()
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

    def test_index(self):
        response = self.client.get('/index/')
        self.assertEquals(response.status_code, 200)


    def test_genre(self):
        response = self.client.get(f'/genre/{self.genre.id}/')
        self.assertEquals(response.status_code, 200)


    def test_book_detail(self):
        response = self.client.get(f'/books/{self.book.id}/')
        self.assertEquals(response.status_code, 200)



