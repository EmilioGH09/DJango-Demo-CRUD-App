from django.urls import path
from . import views

#URL Configuration Model
urlpatterns = [
    path('hello/', views.hello_world)
]