
from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path

urlpatterns = [
    path('members/', include('members.urls')),
    path('page/', lambda request: render(request, 'page.html')),  # Use a different view/template for 'page/'
    path('admin/', admin.site.urls),
    path('home', lambda request: render(request, 'home.html')),  # Use a different view/template for the home page
    path('all_persons/', lambda request: render(request, 'all_persons.html')),  # Use a different view/template for 'all_persons'
    # Make sure 'page.html', 'home.html', and 'all_persons.html' exist in your templates directory.
    path('', lambda request: render(request, 'index.html')),
    path('members/details/<int:id>/', lambda request, id: render(request, 'details.html', {'id': id})),  # Use a different view/template for details
]
