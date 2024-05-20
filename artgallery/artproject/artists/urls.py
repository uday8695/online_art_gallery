from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    
    path('artist/<str:artist_name>',views.artist_details,name='artist_details'),
]
