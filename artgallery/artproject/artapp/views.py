from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def art(request):
    return HttpResponse("<h1>welcome to art gallery</h1>")