from sys import path_hooks
from django.urls import path
#from recipes.views import home, sobre, contato
from recipes.views import receita, home, contato, contato_2, contato_3, receita_2, receita_3
from . import views

# HTTP Request
urlpatterns = [
    path('', views.home),
    path('recipe/<int:id>/', views.recipe),
    path('receita/', receita, name='receita'),
    path('home/', home, name='home'),
    path('contato/', contato, name='contato'),
    path('contato_2/', contato_2, name='contato_2'),
    path('contato_3/', contato_3, name='contato_3'),
    path('receita_2/', receita_2, name='receita_2'),
    path('receita_3/', receita_3, name='receita_3')
]   
