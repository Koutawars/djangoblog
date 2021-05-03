from django.shortcuts import redirect, render
from django.views.generic import FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView

from .forms import UserRegisterForm
from django.contrib.auth.models import User

from django.urls import reverse_lazy

def index(request):
    response = redirect('login/')
    return response

class Register(SuccessMessageMixin, CreateView):
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')
    form_class = UserRegisterForm
    success_message = "La cuenta se ha creado."