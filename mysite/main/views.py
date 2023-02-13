from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item


# Create your views here.


def index(response, id):
    ls = ToDoList.objects.get(id=id)
    item = ls.item_set.get(id=1)
    return HttpResponse("<h1>%s</h1><br><p>%s</p>" % (ls.name, str(item.text)))
