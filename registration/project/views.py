from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Registration
from .forms import RegistrationForm

def create_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_registrations')
    else:
        form = RegistrationForm()
    return render(request, 'create_registration.html', {'form': form})

def view_registrations(request):
    registrations = Registration.objects.all()
    return render(request, 'view_registrations.html', {'registrations': registrations})

def update_registration(request, pk):
    registration = get_object_or_404(Registration, pk=pk)
    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=registration)
        if form.is_valid():
            form.save()
            return redirect('view_registrations')
    else:
        form = RegistrationForm(instance=registration)
    return render(request, 'update_registration.html', {'form': form})

def delete_registration(request, pk):
    registration = get_object_or_404(Registration, pk=pk)
    if request.method == 'POST':
        registration.delete()
        return redirect('view_registrations')
    return render(request, 'delete_registration.html', {'registration': registration})