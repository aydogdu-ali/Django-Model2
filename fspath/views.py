from django.shortcuts import render
from django.http import HttpResponse # respone import ettik.

def selam(request):
    return HttpResponse("<h1>Merhaba Django</h1>") # anasayfada göstermek için bir respone fonksiyonu tanımladım.
