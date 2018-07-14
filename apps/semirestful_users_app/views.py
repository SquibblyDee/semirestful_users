from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

#  import out db
from .models import User

# Create your views here.
def users(request):
    return render(request,'semirestful_users_app/users.html')

def show(request):
    return render(request,'semirestful_users_app/show.html')

def new(request):
    return render(request,'semirestful_users_app/new.html')

def edit(request):
    return render(request,'semirestful_users_app/edit.html')

def process(request, methods=['POST']):
    print("ADD SOME SHIT TO THE DB HERE")