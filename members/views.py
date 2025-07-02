from django.http import HttpResponse
from django.template import loader

def members(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def page(request):
  template = loader.get_template('page.html')
  return HttpResponse(template.render())

def home(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())