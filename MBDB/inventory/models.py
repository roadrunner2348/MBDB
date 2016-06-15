from __future__ import unicode_literals

from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Homeroom(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student_id = models.IntegerField()
    homeroom = models.ForeignKey('Homeroom')
    group = models.ForeignKey('Group', null=True)


    def __str__(self):
        return self.first_name + " " + self.last_name

class Manufacturer(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Model(models.Model):
    name = models.CharField(max_length=30)
    manufacturer = models.ForeignKey('Manufacturer')
    model_number = models.CharField(max_length=30)

    def __str__(self):
        return str(self.manufacturer) + " " + self.name

class Device(models.Model):
    asset_tag = models.IntegerField()
    serial_number = models.CharField(max_length = 20)
    model = models.ForeignKey('Model', null=True)
    student = models.ForeignKey('Student', null=True, blank=True)
    group = models.ForeignKey('Group', null=True, blank=True)
    status = models.ForeignKey('Status', null=True, blank=True)

    def __str__(self):
        return str(self.asset_tag)

class Status(models.Model):
    name = models.CharField(max_length=20)
    checked_out = models.BooleanField()

    def __str__(self):
        return self.name
