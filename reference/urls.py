# reference/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.reference_list, name='reference_list'),
    path('<int:pk>/', views.reference_detail, name='reference_detail'),
]