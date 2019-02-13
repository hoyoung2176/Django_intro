from django.shortcuts import render, HttpResponse
from pprint import pprint
import random

# Create your views here.
def index(request):
    # print(request)
    # print(type(request))
    # pprint(request.META)
    return HttpResponse('Welcome to Django !')
    
def dinner(request):
    menu = ['밥', '국', '김치', '고기', '야채']
    pick = random.choice(menu)
    return render(request, 'dinner.html', {'menus': menu, 'pick': pick})
    
def hello(request, name):
    return render(request, 'hello.html', {'name' : name})
    
def cube(request, num):
    result = num ** 3
    return render(request, 'cube.html', {'num': num, 'result' :result})