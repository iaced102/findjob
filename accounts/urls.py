from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.Register, name = 'SignUp')
]