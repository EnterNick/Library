from django.contrib.auth import get_user_model
from rest_framework import serializers

from book.models import Book, Category


class BookModelSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title', queryset=Category.objects.all())

    class Meta:
        model = Book
        exclude = [
            'author',
        ]
        read_only_fields = [
            'date_created',
        ]

    def save(self, **kwargs):
        user = self.context['request'].user
        return super().save(**{**kwargs, 'author': user})


class BookResponseSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
