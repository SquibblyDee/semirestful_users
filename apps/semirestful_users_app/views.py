from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages #Probably needed for flash erros

#  import our db
from .models import User

# Create your views here.
def users(request):
    #Query and return all the values we need for the app
    query = User.objects.values('id', 'name', 'email', 'created_at')
    return render(request,'semirestful_users_app/users.html', { "query" : query }, {'id' : id})

def show(request, id):
    # Accepts id var from template then does a get 
    # on that id's row before returning it as query
    query = User.objects.filter(id=id).values
    return render(request,'semirestful_users_app/show.html', { "query" : query })

def new(request):
    # The create a new user page
    return render(request,'semirestful_users_app/new.html')

def edit(request, id):
    # Accepts id var from template then does a get 
    # on the needed data from that id's row before returning it as query
    query = User.objects.filter(id=id).values('id', 'name', 'email')
    return render(request,'semirestful_users_app/edit.html', {'query': query})

##This is called when we add a new user from the /users page
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
        #build our values for the name and email keys
        name = request.POST['first_name'] + " " + request.POST['last_name']
        email = request.POST['email']
        #write values to our User tables
        User.objects.create(name=name, email=email)
        messages.success(request, "User table successfully updated")
        id = User.objects.get(name=name).id
        # redirect to a success route
        return redirect('/users/{}'.format(id))

def update(request, methods=['POST']):
    # pass the post data to the method we wrote and save the response in a variable called errors
    # ID was passed into this method by a hidden form which is probably a bad way to do it.
    errors = User.objects.basic_validator(request.POST)
    # check if the errors object has anything in it
    if len(errors):
        # Have to declare this stuff up her too or else the redirect wont work
        id = request.POST['id']
        id = User.objects.get(id=id).id
        # if the errors object contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
            print("WEVE HIT AN ERROR")
        # redirect the user back to the form to fix the errors
        return redirect('/users/{}/edit'.format(id))
    else:
        # if the errors object is empty, that means there were no errors!
        # retrieve the table to be updated, make the changes, and save
        # Update the existing values in the DB table and save
        e = User.objects.get(id=request.POST['id'])
        e.id = request.POST['id']
        e.name = request.POST['first_name']+ " " + request.POST['last_name']
        e.email = request.POST['email']
        e.save()
        messages.success(request, "User table successfully updated")
        id = User.objects.get(id=e.id).id
        # redirect to a success route
        return redirect('/users/{}'.format(id))


def destroy(request, id):
    # Deletes the row of the id that is passed in as a var and print success massage to server 
    User.objects.get(id=id).delete()
    print("DELETED USER RECORD: ", id)
    return redirect('/users')
    