from django.shortcuts import render
from .models import Article, Profile


def show_articles(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(
        request,
        'articles.html',
        context
    )


def show_article(request, id):
    obj = Article.objects.get(id=id)
    user = request.user
    profile = Profile.objects.get(user=user).is_subscribed
    if obj.paid_content and not profile:
        context = {
            'title': obj.title,
            'limited': 'Статья доступна полько по подписке'
        }
    else:
        context = {
            'title': obj.title,
            'body': obj.text
        }
    return render(
        request,
        'article.html',
        context
    )
