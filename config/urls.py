from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/catalog/', include('book.urls')),
    path('catalog/', include('book_front.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('login/', LogoutView.as_view(), name='logout'),
]
