from django.views.generic import TemplateView, DetailView

from book.models import Book


class IndexView(TemplateView):
    template_name = 'index.html'


class BookDetailView(DetailView):
    queryset = Book.objects.all()
    template_name = 'detail.html'

    def post(self, request, *args, **kwargs):
        if request.POST.get('method', 'post') == 'DELETE':
            self.get_object(queryset=Book.objects.all()).delete()
        else:
            return self.get(request, *args, **kwargs)
