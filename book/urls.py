from django.urls import path

from .views import BooksView, BookDetailView, BookAddView

urlpatterns = [
    path('', BooksView.as_view(), name='all_books'),
    path('<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('add/', BookAddView.as_view(), name='book-create'),
]
