from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("complete/<str:pk>", views.complete, name="complete"),
    path("delete/<str:pk>", views.delete, name="delete"),
]
