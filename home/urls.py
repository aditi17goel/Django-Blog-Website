from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('',views.home, name='home'),
    path('contact/',views.contact, name='contact'),
    path('about/',views.about, name='about'),
]