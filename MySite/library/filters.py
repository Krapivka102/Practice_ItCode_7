import django_filters
from library import models


class Book(django_filters.FilterSet):
    title = django_filters.CharFilter(label='Название', lookup_expr='icontains')

    pages__gt = django_filters.NumberFilter(field_name='pages', lookup_expr='gt', label='Кол-во страниц от')
    pages__lt = django_filters.NumberFilter(field_name='pages', lookup_expr='lte', label='Кол-во страниц до')

    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt', label='Цена от')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lte', label='Цена до')

    class Meta:
        model = models.Book
        exclude = ('photo', 'description', 'public_date', 'price', 'pages', )