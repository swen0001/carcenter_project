from django.shortcuts import render, get_object_or_404
from .models import News
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger


def news(request):

    news = News.objects.order_by('-created_date')
    data = {
        'news': news,
    }
    return render(request, 'news/news.html', data)


def news_detail(request, id):
    single_news = get_object_or_404(News, pk=id)

    data = {
        'single_news': single_news,
    }
    return render(request, 'news/news_detail.html', data)

