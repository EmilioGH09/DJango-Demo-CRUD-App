from django.urls import path
from . import views

#URL Configuration Model
urlpatterns = [
    path('/', views.drinks),
    path('/<int:id>', views.drink)
]