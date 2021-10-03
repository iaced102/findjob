from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.urls.base import reverse_lazy

from .models import User

class RegistrationForm(UserCreationForm):
    email               = forms.EmailField(max_length=100)

    # the real name what use to create auto email form
    first_name          = forms.CharField(max_length = 30)
    last_name           = forms.CharField(max_length = 30)

    # the name what display when user create blog or comment
    display_name        = forms.CharField(max_length = 50)
    success_url = reverse_lazy('home')
    

    class Meta:
        model = User
        fields = ("email","username","first_name","last_name","display_name","password1","password2")
        