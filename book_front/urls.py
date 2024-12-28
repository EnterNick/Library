from django.urls import path

from .views import IndexView, BookDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', BookDetailView.as_view(), name='detail'),
]
