from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView

from .filters import CategoryFilter
from .models import Book
from .serializers import BookModelSerializer, BookResponseSerializer


class BooksView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    filterset_class = CategoryFilter

    filter_backends = [
        DjangoFilterBackend,
    ]


class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookResponseSerializer


class BookAddView(CreateAPIView):
    serializer_class = BookModelSerializer
    queryset = Book.objects.all()


class BookGetView(CreateAPIView):
    queryset = Book.objects.all()
