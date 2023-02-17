from nturl2path import url2pathname
from django.shortcuts import render
from django.views import generic
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Password_Manager
from django.contrib.auth.mixins import LoginRequiredMixin
from cryptography.fernet import Fernet
from mechanize import Browser
import favicon
from django.conf import settings


# Create your views here.

br = Browser()
br.set_handle_robots(False)
fernet = Fernet(settings.KEY)

class HomeListView(LoginRequiredMixin, generic.ListView):
    template_name = 'home.html'
    login_url = 'login'


    def get_queryset(self):
        passwords = Password_Manager.objects.filter(user=self.request.user)
        for password in passwords:
            password.email = fernet.decrypt(password.email.encode()).decode()
            password.password = fernet.decrypt(password.password.encode()).decode()
        return passwords

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class PasswordCreateView(LoginRequiredMixin, generic.CreateView):
    model = Password_Manager
    fields = ['url', 'email', 'password']
    template_name = 'add_password.html'
    login_url = 'login'

    def form_valid(self, form):
        url = form.instance.url
        encrypted_email = fernet.encrypt(form.instance.email.encode())
        encrypted_password = fernet.encrypt(form.instance.password.encode())
        try:
            br.open(url)
            title = br.title()
        except:
            title = url
        
        try:
            icon = favicon.get(form.instance.url)[0].url
        except:
            icon = "https://cdn-icons-png.flaticon.com/128/1006/1006771.png"
        
        form.instance.user = self.request.user
        form.instance.name = title
        form.instance.logo = icon
        form.instance.email = encrypted_email.decode()
        form.instance.password = encrypted_password.decode()
        return super().form_valid(form)
            