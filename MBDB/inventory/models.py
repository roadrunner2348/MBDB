from __future__ import unicode_literals

from django.db import models

class Program(model.Models):
    name = models.CharField(max_length=30)

class Homeroom(model.Models):
    name = models.CharField(max_length=10)

class Student(model.Models):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student_id = models.IntegerField()
    homeroom = models.ForeignKey('Homeroom')
    program = models.ForeignKey('Program')

class Manufacturer(model.Models):
    name = models.CharField(max_length=30)

class Model(model.Models):
    name = models.CharField(max_length=30)
    manufacturer = models.ForeignKey('Manufacturer')
    model_number = models.CharField(max_length=30)

class Device(model.Models):
    asset_tag = models.IntegerField()
    serial_number = models.CharField(max_length = 20)
