from django.shortcuts import render, get_object_or_404

from .models import Post, Group

PAGINATION: int = 10


def index(request):
    posts = Post.objects.all()[:PAGINATION]
    context = {
        'posts': posts,
        'title': 'Это главная страница проекта Yatube',
        'text': 'Последние обновления на сайте'
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.group_posts.all()[:PAGINATION]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
