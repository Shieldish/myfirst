
from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path

urlpatterns = [
     path('members/', include('members.urls')),
     path('page/', lambda request: render(request, 'page.html')),  # Use a different view/template for 'page/'
     path('admin/', admin.site.urls),
     path('', lambda request: render(request, 'home.html')),  # Use a different view/template for the home page
]
