from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Group

class GroupListView(ListView):
    model = Group
