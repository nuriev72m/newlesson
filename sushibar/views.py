from django.http import HttpResponse, HttpResponseNotFound, Http404

from django.shortcuts import render, redirect, get_object_or_404
from .models import *

menu = [{'title': 'Главная', 'url_name': 'home'},
        {'title': 'Сашими', 'url_name': 'sashimi'},
        {'title': 'Суши', 'url_name': 'sushi'},
        {'title': 'Роллы', 'url_name': 'rolls'},
        {'title': 'Прайс-лист', 'url_name': 'pricelist'}
        ]


def index(request):
    posts = Sashimi.objects.all()
    #cats = Category.objects.all()
    context = {
        'posts': posts,
        # 'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'sushibar/index.html', context=context)


def sashimi(request):
    posts = Sashimi.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Сашими'
    }
    return render(request, 'sushibar/sashimi.html', context=context)


def sushi(request):
    return HttpResponse("Суши")


def rolls(request):
    return HttpResponse("Роллы")


def pricelist(request):
    return HttpResponse("Прайс-лист")


def show_post(request, post_id):
    post = get_object_or_404(Sashimi, pk=post_id)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': 1,
    }

    return render(request, 'sushibar/post.html', context=context)


def show_category(request, cat_id):
    #posts = Sashimi.objects.filter(cat_id=cat_id)
    #cats = Category.objects.all()
    cw = Category.objects.get(pk=cat_id)
    #posts = cw.entries.all()
    if cw.name == 'Сашими':
        posts = cw.sashimi_set.all()
    elif cw.name == 'Суши':
        posts = cw.sushi_set.all()
    else:
        posts = cw.rolls_set.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        # 'cats': cats,
        'menu': menu,
        'title': cw.name,
        'cat_selected': cat_id,
    }
    return render(request, 'sushibar/sashimi.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
