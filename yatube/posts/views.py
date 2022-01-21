from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    context = {
        'title' : title,
    }
    return render(request, template, context)

def group_details(response, any_slug):
    return HttpResponse(f'Страница {any_slug}')

def group_list(request):
    template = 'posts/group_list.html'
    title = 'Лев Толстой – зеркало русской революции.'
    context = {
        'title' : title,
    }
    return render(request, template, context)
