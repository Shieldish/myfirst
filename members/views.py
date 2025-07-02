from django.http import HttpResponse
from django.template import loader

def members(request):
  # Define the dataset directly instead of using the Person model
  mymembers = [
    {'id': 1, 'first_name': 'John', 'last_name': 'Doe'},
    {'id': 2, 'first_name': 'Jane', 'last_name': 'Smith'},
    {'id': 3, 'first_name': 'Alice', 'last_name': 'Johnson'},
  ]
  template = loader.get_template('index.html')
  context = {'mymembers': mymembers}
  print(context)
  return HttpResponse(template.render(context, request))

def page(request):
  template = loader.get_template('page.html')
  print("Page accessed")  # This will print to your server console
  return HttpResponse(template.render({}, request))

def home(request):
  template = loader.get_template('index.html')
  print("Home page accessed")  # This will print to your server console
  return HttpResponse(template.render({}, request))

def all_persons(request):
  from .models import Person  # Use relative import
  mymembers = Person.objects.all()
  print( Person.objects.all())  # This will print to your server console, not browser!
  template = loader.get_template('all_persons.html')
  context = {'mymembers': mymembers}
  return HttpResponse(template.render(context, request))

from .models import Person  # Import the Person model
def details(request, id):
  mymember =  [
    {'id': 1, 'first_name': 'John', 'last_name': 'Doe'},
    {'id': 2, 'first_name': 'Jane', 'last_name': 'Smith'},
    {'id': 3, 'first_name': 'Alice', 'last_name': 'Johnson'},
  ]
  print(mymember)  # This will print to your server console, not browser!
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))