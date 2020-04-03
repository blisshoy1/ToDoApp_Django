from django.shortcuts import render
from .models import Do
from django.http import HttpResponseRedirect


# Create your views here.

def index(request):
    mydo = Do.objects.all()
    return render(request, 'index.html',{'mydo':mydo})


def addtodo(request):
    new_item = Do(things=request.POST['details'])
    new_item.save()
    return HttpResponseRedirect('/')

def deletetodo(request, d_id):
    item_to_delete= Do.objects.get(id=d_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/')
