from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to my book store.")

def another(request):
    return HttpResponse("Check this out!")

def example(request):
    anything = {"name": "Mamy"}
    return render(request, "book_store/hello.html", anything)