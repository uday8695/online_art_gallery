from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def art(request):
#     return HttpResponse("<h1>welcome to art gallery</h1>")

def header(request):
    return render(request,'header.html')

def footer(request):
    return render(request,'footer.html')

def home(request):
    return render(request,'home.html')

def artists(request):
    return render(request,'artists.html')

def shop(request):
    return render(request,'shop.html')

def artsupplies(request):
    return render(request,'artsupplies.html')

def styles(request):
    return render(request,'styles.html')

def Login(request):
    return render(request,'Login.html')

def Register(request):
    return render(request,'Register.html')