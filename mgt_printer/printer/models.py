from secrets import choice
from django.db import models

# Create your models here.
class Printer(models.Model):
  printer_name= models.CharField(max_length=255)
  driver= models.CharField(max_length=255)
  manufacture= models.CharField(max_length=255)
  ip_address = models.CharField(max_length=255)
  lokasi = models.CharField(max_length=255)
  warnatipe = models.TextChoices('Monochrome', 'Berwarna')
  warna = models.CharField(blank=True, choices=warnatipe.choices, max_length=255)

class User(models.Model):
  nama_user = models.CharField(max_length=255)
  jabatan = models.CharField(max_length=255)
  PIC = models.IntegerField()

class Maintenance(models.Model):
  last_mt = models.DateField()
  cause = models.TextField()
  supplier_tinta = models.CharField(max_length=255)
  mt_store = models.CharField(max_length=255)
  count_mt = models.IntegerField()
  tgl_beli = models.DateField()

class Operational(models.Model):
  kertas_tipe = models.TextChoices('A4', 'F4')
  kertas = models.CharField(blank=True, choices=kertas_tipe.choices, max_length=10)
  server_tipe = models.TextChoices('CUPS Server', 'IP Server')
  server = models.CharField(blank=True, choices=server_tipe.choices, max_length=40)
  support_tipe = models.TextChoices('Support Linux', 'Non-Support Linux')
  support = models.CharField(blank=True, choices=support_tipe.choices, max_length=50, default="")
  usb_lan_wifi_tipe = models.TextChoices('USB', 'USB,LAN,WIFI')
  usb_lan_wifi = models.CharField(blank=True, choices=usb_lan_wifi_tipe.choices, max_length=100)

  
