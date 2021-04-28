from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    extas_data={'name':'Deepak','Surname':'Suryawanshi','age':20,'address':'B-193, shakti nagar korba'}
    return render(request,'index.html',extas_data)