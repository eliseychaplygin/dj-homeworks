from django.views.generic import ListView
from django.shortcuts import render

from .models import Article


def articles_list(request):
    template_name = 'articles/news.html'
    data = Article.objects.defer('published_at').select_related('author', 'genre').defer('author__phone')

    context = {
        'object_list': data,
    }

    return render(request, template_name, context)
