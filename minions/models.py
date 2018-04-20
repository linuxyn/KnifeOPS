from django.db import models

# Create your models here.


class Host(models.Model):
    hostname = models.CharField(max_length=64)
    ip = models.GenericIPAddressField(protocol="ipv4")
    cabinet = models.IntegerField(max_length=32)
    room = models.CharField(max_length=64)
    cpu_model = models.CharField(max_length=128)
    cpu_core = models.IntegerField(max_length=128)
    mem = models.IntegerField(max_length=32)
    disk = models.IntegerField(max_length=32)
    os = models.CharField(max_length=128)
    product_model = models.CharField(max_length=128)
    business_id = models.ForeignKey("Business")


class Business(models.Model):
    name = models.CharField(max_length=64)
    describe = models.CharField(max_length=128)


