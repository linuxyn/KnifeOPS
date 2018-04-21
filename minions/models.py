from django.db import models

# Create your models here.


class Host(models.Model):
    """资产信息表"""
    hostname = models.CharField(max_length=64, unique=True, null=False)
    ip = models.GenericIPAddressField(protocol="ipv4", unique=True, null=False)
    cabinet = models.IntegerField()
    cpu_model = models.CharField(max_length=128)
    cpu_core = models.IntegerField()
    mem = models.IntegerField()
    disk = models.IntegerField()
    OS = models.CharField(max_length=128)
    product_model = models.CharField(max_length=128)
    minions_status = models.CharField(max_length=32, default="undefined")
    business = models.ForeignKey("Business", null=False)
    room = models.ForeignKey("Room", null=False)


class Business(models.Model):
    """业务线信息"""
    name = models.CharField(max_length=64)
    describe = models.CharField(max_length=128)


class Room(models.Model):
    """机房信息表"""
    name = models.CharField(max_length=128)
    detail = models.CharField(max_length=256)


