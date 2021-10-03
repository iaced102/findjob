from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.Registration_view, name = 'signup')
]