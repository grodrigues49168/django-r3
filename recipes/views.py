from django.shortcuts import render
from django.http import HttpResponse
from utils.recipes.factory import make_recipe
# Create your views here.

# HTTP Request
def home(request):
    return render(request, 'recipes/pages/home.html', context={
         'name': 'Byanna Burguer',
    })

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(), 'name': 'Byanna Burguer',
        'is_detail_page' : True,
    })

def receita(request):
    return render(request,'recipes/part/receita.html', context={'name': 'Byanna Burguer'})

def receita_2(request):
    return render(request,'recipes/part/receita_2.html', context={'name': 'Byanna Burguer'})

def receita_3(request):
    return render(request,'recipes/part/receita_3.html', context={'name': 'Byanna Burguer'})

def contato(request):
    return render(request,'recipes/part/contato.html', context={'name': 'Byanna Burguer'})

def contato_2(request):
    return render(request,'recipes/part/contato_2.html', context={'name': 'Byanna Burguer'})

def contato_3(request):
    return render(request,'recipes/part/contato_3.html', context={'name': 'Byanna Burguer'})
  
# def contato(request):
#     # HTTP Response
#     return HttpResponse('')
