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
    # pass the post data to the method we wrote and save the response in a variable called errors
    errors = User.objects.basic_validator(request.POST)
    # check if the errors object has anything in it
    if len(errors):
        # if the errors object contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
            print("WEVE HIT AN ERROR")
        # redirect the user back to the form to fix the errors
        return redirect('/users/new')
    else:
        # if the errors object is empty, that means there were no errors!
        # retrieve the blog to be updated, make the changes, and save
        name = request.POST['first_name'] + " " + request.POST['last_name']
        print(name)
        email = request.POST['email']
        print(email)
        User.objects.create(name=name, email=email)
        # user.email = email
        # user.save()
        messages.success(request, "User table successfully updated")
        # redirect to a success route
        return redirect('/users/new')
    
    # if request.method == "POST":
        # print("*"*50)
        # print(request.POST)
        # name = request.POST['first_name'] + " " + request.POST['last_name']
        # print(name)
        # print(request.POST['email'])
        # print("*"*50)
        # return redirect("/users")
    # else:
        # return redirect("/users")

def destroy(request):
    print("DELETE SELECTED USER HERE")
    return redirect('/users')