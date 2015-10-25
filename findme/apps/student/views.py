from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    render(request, 'home.html', {})
