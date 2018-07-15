from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages #Probably needed for flash erros
from django.db.models.functions import Concat #Probably needed for concatenation

#  import our db
from .models import User

# Create your views here.
def users(request):
    #Query and return all the values we need for the app
    query = User.objects.values('id', 'name', 'email', 'created_at')
    return render(request,'semirestful_users_app/users.html', { "query" : query }, {'id' : id})

def show(request, id, methods=['POST']):
    query = User.objects.values('id')
    print("GOT DAT IDDDDDDDDDD", id)
    query = User.objects.filter(id=id).values
    print("NEW QUERRRRYYYYY", query)
    return render(request,'semirestful_users_app/show.html', { "query" : query })

def new(request):
    return render(request,'semirestful_users_app/new.html')

def edit(request, id):
    print(id)
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
        # retrieve the table to be updated, make the changes, and save
        #build our calues for the name and email keys
        name = request.POST['first_name'] + " " + request.POST['last_name']
        email = request.POST['email']
        #write values to our User tables
        User.objects.create(name=name, email=email)
        messages.success(request, "User table successfully updated")
        id = User.objects.get(name=name).id
        # redirect to a success route
        print("REDIRECTINGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG")
        return HttpResponseRedirect('/users/{}'.format(id))
    

def destroy(request):
    print("DELETE SELECTED USER HERE")
    return redirect('/users')
    