from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'shop/index.html')

def contact(request):
    return render(request,'shop/contact.html')

def tracker(request):
    return render(request,'shop/trackorder.html')

def about(request):
    return render(request,'shop/aboutus.html')

def search(request):
    return HttpResponse('Search')

def prodview(request):
    return HttpResponse('Product')

def checkout(request):
    return render(request,'shop/checkout.html')

def login(request):
    return render(request,'shop/login.html')

def test(request):
    return render(request,'shop/test.html')

def cart(request):
    return render(request,'shop/cart.html')