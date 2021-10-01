from django.shortcuts import render
from . import forms
from django.http import HttpResponseRedirect
from django.views.generic import CreateView

def Register(request):
    form = forms.RegistrationForm()
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('.')
    return render(request, 'registrations/signup.html', {'form': form})