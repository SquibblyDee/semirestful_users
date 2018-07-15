from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages #Probably needed for flash erros
from django.db.models.functions import Concat #Probably needed for concatenation

#  import our db
from .models import User

# Create your views here.
def users(request):
    query = User.objects.values('id', 'name', 'email', 'created_at')
    return render(request,'semirestful_users_app/users.html', { "query" : query })

def show(request, num):
    return render(request,'semirestful_users_app/show.html')

def new(request):
    return render(request,'semirestful_users_app/new.html')

def edit(request, num):
    print(num)
    return render(request,'semirestful_users_app/edit.html')

def create(request, methods=['POST']):
    if request.method == "POST":
        print("*"*50)
        print(request.POST)
        print(request.POST['first_name'])
        print(request.POST['last_name'])
        #temp = Concat(request.POST['first_name'], request.POST['last_name'])
        temp = request.POST['first_name']
        temp2 = request.POST['last_name']
        name = (temp+" "+temp2)
        print(name)
        print(request.POST['email'])
        # request.session['name'] = "test"  # more on session below
        print("*"*50)
        return redirect("/users")
    else:
        return redirect("/users")

def destroy(request):
    print("DELETE SELECTED USER HERE")
    return redirect('/users')