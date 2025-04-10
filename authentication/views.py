from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .froms import CustomUserCreationForm
from . import models
# Create your views here.
class SignUpView(CreateView):
    model = models.CustomUser
    form_class = CustomUserCreationForm
    template_name = 'authentication/signup.html'
    success_url = reverse_lazy('login')