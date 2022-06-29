from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Operational, Printer, User, Maintenance

# Create your views here.

def index(request):
  myprinter = Printer.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'myprinter': myprinter,
  }
  return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  a = request.POST['printer_name']
  b = request.POST['driver']
  c = request.POST['manufacture']
  d = request.POST['ip_address']
  e = request.POST['lokasi']
  f = request.POST['warna']
  printer = Printer(printer_name=a, driver=b, manufacture=c, ip_address=d, lokasi=e, warna=f)
  printer.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  printer = Printer.objects.get(id=id)
  printer.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  myprinter = Printer.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'myprinter': myprinter,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  a = request.POST['printer_name']
  b = request.POST['driver']
  c = request.POST['manufacture']
  d = request.POST['ip_address']
  e = request.POST['lokasi']
  f = request.POST['warna']
  printer = Printer.objects.get(id=id)
  printer.printer_name = a
  printer.driver = b
  printer.manufacture = c
  printer.ip_address = d
  printer.lokasi = e
  printer.warna = f
  printer.save()
  return HttpResponseRedirect(reverse('index'))

def users(request):
  myuser = User.objects.all().values()
  template = loader.get_template('users.html')
  context = {
    'myuser': myuser,
  }
  return HttpResponse(template.render(context, request))

def mt(request):
  mymt = Maintenance.objects.all().values()
  template = loader.get_template('mt.html')
  context = {
    'mymt': mymt,
  }
  return HttpResponse(template.render(context, request))

def ops(request):
  myops = Operational.objects.all().values()
  template = loader.get_template('ops.html')
  context = {
    'myops': myops,
  }
  return HttpResponse(template.render(context, request))