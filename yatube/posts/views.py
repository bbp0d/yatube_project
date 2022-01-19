from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return HttpResponse('Главная страница')

def group_details(response, any_slug):
    return HttpResponse(f'Страница {any_slug}')
