from django.shortcuts import render,redirect

def index(request):
    context = {
        'name': 'Desconegut'
    }
    return render(request,'hello/index.html',context)

