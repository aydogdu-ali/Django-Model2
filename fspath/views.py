from django.shortcuts import render
from django.http import HttpResponse

def selam(request):
    return HttpResponse("<h1>Merhaba Django</h1>")
