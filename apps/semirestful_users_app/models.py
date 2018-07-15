from __future__ import unicode_literals
from django.db import models
# Create your models here.

# This class handles all of the validation for our forms on submit
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 3:
            errors["first_name"] = "First name should be at least 3 characters"
        if len(postData['last_name']) < 3:
            errors["last_name"] = "Last name should be at least 3 characters"
        if "@" not in postData['email']:
            errors["email"] = "Email needs to have an @"
        return errors

# This is our table
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    # *************************
    # Connect an instance of BlogManager to our Blog model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    objects = UserManager()
    # *************************
