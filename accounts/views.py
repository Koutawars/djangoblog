from django.shortcuts import redirect, render
from django.views.generic import FormView
from django.contrib.auth.models import User

from django.urls import reverse_lazy

def index(request):
    response = redirect('login/')
    return response
