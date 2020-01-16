from django.shortcuts import render, get_object_or_404
from .models import Category, News


def news_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    news = News.objects.filter(status=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        news = news.filter(category=category)

    return render(request, 'news_list.html', {'category': category,
                                              'categories': categories,
                                              'news': news,
                                              })


def post_detail(request, post_id):
    post = get_object_or_404(News, id=post_id)
    return render(request, 'details.html', {'post': post})


