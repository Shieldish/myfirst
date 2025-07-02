
from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('page/', views.members, name='page'),
    path('/home', views.members, name='home'),
    path('', views.members, name='index'),
    path('all_persons/', views.members, name='all_persons'),
    path('members/details/<int:id>', views.details, name='details'),
  
]
# There is nothing missing here. Your urlpatterns are correctly defined.
