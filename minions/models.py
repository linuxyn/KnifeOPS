from django.db import models

# Create your models here.


class Host(models.Model):
    """资产信息表"""
    hostname = models.CharField(max_length=64, unique=True)
    ip = models.GenericIPAddressField(protocol="ipv4", unique=True)
    cabinet = models.IntegerField(null=True)
    cpu_model = models.CharField(max_length=128, null=True)
    cpu_core = models.IntegerField(null=True)
    mem = models.IntegerField(null=True)
    disk = models.IntegerField(null=True)
    OS = models.CharField(max_length=128, null=True)
    product_model = models.CharField(max_length=128, null=True)
    minions_status = models.CharField(max_length=32, null=True, default="undefined")
    business = models.ForeignKey("Business")
    room = models.ForeignKey("Room")


class Business(models.Model):
    """业务线信息"""
    name = models.CharField(max_length=64)
    describe = models.CharField(max_length=128, null=True)


class Room(models.Model):
    """机房信息表"""
    name = models.CharField(max_length=128)
    detail = models.CharField(max_length=256,null=True)


