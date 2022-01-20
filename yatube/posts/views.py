from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    template = 'posts/index.html'
    return render(request, template)

def group_details(response, any_slug):
    return HttpResponse(f'Страница {any_slug}')
