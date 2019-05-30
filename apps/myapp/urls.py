from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('leaveFriendsTrip/<trip_id>', views.leaveFriendsTrip),
    path('deleteTrip/<trip_id>', views.deleteTrip),
    path('joinTrip/<trip_id>', views.joinTrip),
    path('showTrip/<trip_id>', views.showTrip),
    path('trip/create', views.create_trip),
    path('newtrip', views.newtrip),
    path('logout', views.logout),
    path('dashboard', views.dashboard),
    path('users/create', views.create_user),    
    path('login', views.login)
]