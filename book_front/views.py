from django.shortcuts import redirect
from django.views.generic import TemplateView, DetailView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer

from book.models import Book
from book.serializers import BookModelSerializer


class IndexView(TemplateView):
    template_name = 'index.html'


class BookDetailView(DetailView):
    queryset = Book.objects.all()
    template_name = 'detail.html'

    def post(self, request, *args, **kwargs):
        if request.POST.get('method', 'post') == 'DELETE':
            self.get_object(queryset=Book.objects.all()).delete()
        if request.POST.get('method', 'post') == 'PUT':
            serializer = BookModelSerializer(instance=self.get_object(), data=request.POST, context={'request': request})
            if serializer.is_valid():
                serializer.save()
            return redirect('detail', pk=self.get_object().id)
        else:
            return self.get(request, *args, **kwargs)


class BookAddView(CreateAPIView):
    serializer_class = BookModelSerializer
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'create.html'
