from django.http import HttpResponse
from django.shortcuts import render

def index(request): #в реквест попадает экземпляр класс ( анонимный, зарегистр., куки и т.д.) Это называется контролер, а не ф-ция.
    context : dict[str, str] ={
        'title': 'Home',
        'content': 'Главная страница магазина - Home'
    }
    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse('About Page')
