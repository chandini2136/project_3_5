from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def srujana(request):
    return HttpResponse('<h1><marquee>Srujana is a wise girl<marquee></h1>')

def meghana(request):
    return HttpResponse('<h1><marquee>Meghana knows programming well<marquee></h1>')