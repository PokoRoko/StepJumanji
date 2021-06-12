from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

from accounts.forms import MyUserCreationForm


class RegisterView(CreateView):
    form_class = MyUserCreationForm
    success_url = 'login'
    template_name = '../templates/registration /register.html'


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = '../templates/registration /login.html'
