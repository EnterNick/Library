import datetime

from django.contrib.auth import get_user_model
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=100)

    desc = models.CharField(max_length=1000)

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    date_created = models.DateField(default=datetime.date.today)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class BookRequest(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    date_created = models.DateField(datetime.date.today)
