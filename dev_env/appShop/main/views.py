from django.http import HttpResponse
from django.shortcuts import render
from goods.models import  Categories
def index(request): #в реквест попадает экземпляр класс ( анонимный, зарегистр., куки и т.д.) Это называется контролер, а не ф-ция.



    context : dict[str, str] ={
        'title': 'Home - Главная',
        'content': 'Магазин мебели Home',
    }
    return render(request, 'main/index.html', context)

def about(request):
    context: dict[str, str] = {
        'title': 'HOME - О нас',
        'content': 'О нас',
        'text_on_page': 'Rsdfds sd fsdf sdf sdf ds fsd sd fds fds d ssdf',
    }
    return render(request, 'main/about.html', context)
