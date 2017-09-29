from django.shortcuts import render


def index(request):
    context = {
        'name': 'Desconegut'
    }
    return render(request,'hello/hello.html',context)
    # TODO: fer una plantilla amb el boto de login
    # TODO: fer la url de callback que guardi la info a la sessio
    # TODO: recarregar la plantilla
