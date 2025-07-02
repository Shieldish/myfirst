
from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('page/', views.members, name='page'),
    path('', views.members, name='home'),
]

