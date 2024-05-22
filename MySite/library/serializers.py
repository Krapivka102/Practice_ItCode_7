from rest_framework import serializers

from library import models

class Book(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = '__all__'