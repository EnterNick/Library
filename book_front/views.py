from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class BookDetailView(TemplateView):
    template_name = 'detail.html'
