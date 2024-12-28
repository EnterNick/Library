from rest_framework import serializers

from book.models import Book, Category, BookRequest


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

    def get_fields(self):
        fields = super().get_fields()
        for i in fields:
            i.required = False
        return fields


class BookResponseSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    category = serializers.SlugRelatedField(slug_field='title', queryset=Category.objects.all())

    class Meta:
        model = Book
        fields = '__all__'


class BookRequestSerializer(serializers.ModelSerializer):
    book = serializers.SerializerMethodField()

    class Meta:
        model = BookRequest
        fields = '__all__'

    @staticmethod
    def get_book(book_request):
        return BookResponseSerializer(book_request.book).data

    def save(self, **kwargs):
        user = self.context['request'].user
        return super().save(**{**kwargs, 'author': user})
