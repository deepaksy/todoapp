from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    params={'name':'Deepak','Surname':'Suryawanshi','age':20,'address':'B-193, shakti nagar korba','content':'MyAwesomeCart'}
    return HttpResponse("<h1>mac home</h1><br/> <a href='/shop'><h4>Shop</h4></a><br/> <a href='/blog'><h4>Blog</h4></a>")