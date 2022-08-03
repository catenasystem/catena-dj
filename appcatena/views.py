from django.shortcuts import render
from django.http import HttpResponse
from .models import User

itens_menu = User.objects.all()

dados ={'titulo_link_menu':itens_menu}
def index(request):
    return render(request,'index.html',dados)
def mba(request):
    return render(request,'mba.html',dados)
