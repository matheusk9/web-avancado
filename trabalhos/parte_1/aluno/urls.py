from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('matriculas/<int:id>', views.matriculas, name="matriculas"),
    path('contato', views.contato, name="contato"),
]