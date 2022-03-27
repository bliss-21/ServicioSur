from re import template
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

LOGOUT_REDIRECT_URL = 'https://www.google.com/'

urlpatterns = [
    path('', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),   
]