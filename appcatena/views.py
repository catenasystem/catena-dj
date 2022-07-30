from django.shortcuts import render
from django.http import HttpResponse

itens_menu = {
    1:'Inicial',
    2:'Cumprimento de MBA',
    3:'Acompanhamento Operação',
    4:'Visão por etapa'
}
dados ={'titulo_link_menu':itens_menu}
def index(request):
    return render(request,'index.html',dados)
def mba(request):
    return render(request,'mba.html',dados)
