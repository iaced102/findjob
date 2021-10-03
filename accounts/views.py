from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm
from django.urls import reverse_lazy


def Registration_view(request):
    context = {}
    print(request)
    print(request.POST)
    if request.POST:
        print('request is post')
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            password = form.cleaned_data.get('password1')
            username = form.cleaned_data.get('username')
            account = authenticate(username= username, password=password)
            login(request, account)
            form.success_url = reverse_lazy('home')
            return redirect('home')                
        else:
            context['registration_form'] = form
            return render(request, 'registrations/signup.html', context)
    else:
        print('request is GET')
        
        form = RegistrationForm()
        print('reverselazy',form.success_url)
        context['registration_form'] = form
        return render(request, 'registrations/signup.html', context)