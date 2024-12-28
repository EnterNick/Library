from django_filters import FilterSet, ChoiceFilter

from book.models import Category, Book


class CategoryFilter(FilterSet):
    category = ChoiceFilter(
        initial=None,
        choices=Category.objects.values_list('title', 'title'),
        lookup_expr='title',
    )

    class Meta:
        model = Book
        fields = ['category']
