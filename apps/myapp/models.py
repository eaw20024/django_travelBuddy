from django.db import models
from datetime import datetime
import bcrypt

timenow = str(datetime.now())

class UserManager(models.Manager):
    def regValidator(self, form):
        errors = {}
        if not form['name']:
            errors['name'] = 'Name cannot be blank'
        elif len(form['name']) < 3:
            errors['name'] = 'Name must be atleast three characters'
        if not form['username']:
            errors['username'] = 'Username cannot be blank'
        elif len(form['username']) < 3:
            errors['username'] = 'Username must be atleast three characters'
        else:
            users = User.objects.filter(username=form['username'])
            if users:
                errors['username'] = "User is already in database"
        if not form['password']:
            errors['password'] = 'Password cannot be blank'
        elif len(form['password']) < 8:
            errors['password'] = 'Password must be atleast eight characters'
        if form['confirm_password'] != form['password']:
            errors['confirm_password'] = 'Passwords do not match!'
        return errors
    
    def loginValidator(self, form):
        errors = {}
        if not form['pwd']:
            errors['pwd'] = 'Password cannot be blank'
        if not form['username']:
            errors['username'] = 'Email cannot be blank'
        else:
            users = User.objects.filter(username=form['username'])
            if not users:
                errors['username'] = 'This username doesnt exist. Please register!'
            elif not bcrypt.checkpw(form['pwd'].encode(), users[0].password.encode()):
                errors['pwd'] = 'Wrong password'
            return errors
        return errors

class TripManager(models.Manager):
    def tripValidator(self, form):
        errors = {}
        if not form['destination']:
            errors['destination'] = 'Destination cannot be blank'
        if not form['description']:
            errors['description'] = 'Description cannot be blank'
        if not form['travelStart']:
            errors['travelStart'] = 'Please enter a date'
        if not form['travelStart']:
            errors['travelStart'] = 'Please enter a date'
        elif form['travelStart'] < timenow:
            errors['travelEnd'] = 'Nice try! Adding Past dates wont work friend!'
        elif form['travelStart'] > form['travelEnd']:
            errors['travelEnd'] = 'You cannot travel back in time!'
        return errors

class User(models.Model):
    name = models.CharField(max_length=45) 
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()

class Trip(models.Model):
    destination = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    travelStart = models.DateTimeField()
    travelEnd = models.DateTimeField()
    added_by = models.ForeignKey(User, related_name='trips', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = TripManager()

class Join(models.Model):
    user = models.ForeignKey(User, related_name='favorites', on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, related_name='favorites', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)