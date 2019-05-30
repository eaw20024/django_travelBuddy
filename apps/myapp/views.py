from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'index.html')

def create_user(request):
    errors = User.objects.regValidator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.add_message(request, messages.ERROR, value, key)
        return redirect("/")
    password_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    user = User.objects.create(name=request.POST['name'], username=request.POST['username'], password=password_hash.decode())
    request.session['id'] = user.id   
    return redirect("/dashboard")

def dashboard(request):
    if 'id' in request.session:
        user = User.objects.get(id=request.session['id'])
        trips = Trip.objects.all()
        joins = Join.objects.filter(user_id=request.session['id'])
        notFavs = []
        favs = []

        for join in joins:
            favs.append(join.trip_id)

        for trip in trips:
            if trip.id not in favs:
                notFavs.append(trip)
                
        context = {
            "user": user,
            "trips": trips,
            "joins": joins,
            "notFavs": notFavs
        }
        return render(request, 'dashboard.html', context)
    return redirect("/")
    
def login(request):
    errors = User.objects.loginValidator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.add_message(request, messages.ERROR, value, key)
        return redirect("/")
    else:
        users = User.objects.filter(username=request.POST['username'])
        request.session['id'] = users[0].id
    return redirect("/dashboard")

def create_trip(request):
    errors = Trip.objects.tripValidator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.add_message(request, messages.ERROR, value, key)
        return redirect("/newtrip")
    trip = Trip.objects.create(destination=request.POST['destination'], description=request.POST['description'], added_by_id=request.session['id'], travelStart=request.POST['travelStart'], travelEnd=request.POST['travelEnd'])
    
    Join.objects.create(trip=trip, user_id=request.session['id'])
    return redirect("/dashboard")

def newtrip(request):
    return render(request, "newtrip.html")

def showTrip(request, trip_id):
    context = {
        "trip": Trip.objects.get(id=trip_id),
        "users_who_fav_trip": Join.objects.filter(trip_id=trip_id)
    }
    return render(request, 'viewtrip.html', context)

def joinTrip(request, trip_id):
    Join.objects.create(trip_id=trip_id, user_id=request.session['id'])
    return redirect("/dashboard")

def leaveFriendsTrip(request, trip_id):
    Join.objects.get(trip_id=trip_id, user_id=request.session['id']).delete()
    return redirect('/dashboard')

def deleteTrip(request, trip_id):
    Trip.objects.get(id=trip_id).delete()
    return redirect('/dashboard')

def logout(request):
    request.session.clear()
    print("Logged Out")
    return redirect("/")