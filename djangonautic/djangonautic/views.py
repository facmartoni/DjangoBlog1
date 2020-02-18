from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse('pagina nativa')
    return render(request,'home.html')

def about(request):
    #return HttpResponse('acerca de')
    return render(request,'about.html')