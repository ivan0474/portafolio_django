from django.http import HttpResponse
from django.template import Template, Context

def inicio(request):
    doc_externo = open("static/index.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento= plt.render(ctx)
    return HttpResponse(documento)
    
def historial(request):
    doc_externo = open("static/historial.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento= plt.render(ctx)
    return HttpResponse(documento)

def Productos(request):
    doc_externo = open("static/Productos.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento= plt.render(ctx)
    return HttpResponse(documento)

def Seguimiento(request):
    doc_externo = open("static/Seguimiento.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento= plt.render(ctx)
    return HttpResponse(documento) 
    
def login(request):
    doc_externo = open("static/login.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento= plt.render(ctx)
    return HttpResponse(documento)
    
def Register(request):
    doc_externo = open("static/Register.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento= plt.render(ctx)
    return HttpResponse(documento)   

def index(request):
    doc_externo = open("static/index.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context()
    documento= plt.render(ctx)
    return HttpResponse(documento)

#Redirecciones:

from django.shortcuts import redirect

def redirect_index(request):
    response = redirect('/index/')
    return response

def redirect_Productos(request):
    return redirect('/Productos/')

def redirect_Seguimiento(request):
    return redirect('/Seguimiento/')

def redirect_historial(request):
    return redirect('/historial/')

def redirect_login(request):
    return redirect('')
