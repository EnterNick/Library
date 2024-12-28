from django.urls import path

from .views import IndexView, BookDetailView, BookAddView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', BookDetailView.as_view(), name='detail'),
    path('add/', BookAddView.as_view(), name='create'),
]
