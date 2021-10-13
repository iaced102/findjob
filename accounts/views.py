from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm
from django.urls import reverse_lazy

def Registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            password = form.cleaned_data.get('password1')
            username = form.cleaned_data.get('username')
            account = authenticate(username= username, password=password)
            login(request, account)
            return redirect('home')                
        else:
            context['registration_form'] = form
            return render(request, 'registrations/signup.html', context)
    else:
        form = RegistrationForm()
        context['registration_form'] = form
        return render(request, 'registrations/signup.html', context)
