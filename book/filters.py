from django_filters import FilterSet, ChoiceFilter

from book.models import Category, Book


class CategoryFilter(FilterSet):
    category = ChoiceFilter(
        initial='1',
        choices=Category.objects.values_list('id', 'title'),
    )

    class Meta:
        model = Book
        fields = ['category']
