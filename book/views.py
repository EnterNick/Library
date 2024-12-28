from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .filters import CategoryFilter
from .models import Book, BookRequest
from .serializers import BookModelSerializer, BookResponseSerializer, BookRequestSerializer


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
    permission_classes = [IsAuthenticated]


class BookAddView(CreateAPIView):
    serializer_class = BookModelSerializer
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()


class BookGetView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BookRequest.objects.all()
    serializer_class = BookRequestSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
