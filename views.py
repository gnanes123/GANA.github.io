from django.http import HttpResponse
from django.template import loader

def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())
def about(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render())
def services(request):
  template = loader.get_template('services.html')
  return HttpResponse(template.render())
def contact(request):
  template = loader.get_template('contact.html')
  return HttpResponse(template.render())