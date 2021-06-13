from django.contrib.auth.views import LogoutView
from django.urls import include, path

from accounts.views import MyLoginView, RegisterView

urlpatterns = [
    path('login/', MyLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', RegisterView.as_view(), name="register"),
    path('accounts/', include('django.contrib.auth.urls')),
]
