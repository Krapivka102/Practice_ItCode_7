from django.test import TestCase, Client
from library import models


class Test(TestCase):
    def SetUp(self):
        self.client = Client()
        self.book = models.Book.objects.create(
            title="Ведьмак 1",
            author="Сапковский",
            description="Некое описание книги",
            genre=1,
            pages=120,
            price=300,
        )


