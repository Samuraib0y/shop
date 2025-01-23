from django.urls import path
from main import views as mainViews

app_name = 'main'
urlpatterns = [
    path('', mainViews.index, name='index'),
    path('about/', mainViews.about, name='about'),
]
