# arquivo views.py do app sistema
from django.shortcuts import render

def index(request):
    return render(
        request,
        'sistema/index.html',
    )