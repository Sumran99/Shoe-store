from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about", views.about, name="about"),
    path("featured", views.featured, name="featured"),
    path("kids", views.kids, name="kids"),
    path("contact", views.contact, name="contact")
]
