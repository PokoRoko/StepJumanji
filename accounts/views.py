from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView


class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'register.html'


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'
