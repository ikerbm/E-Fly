from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CreateUserForm()

    context = {'form': form}     
    return render(request, 'vuelos/userRegister.html', context)

# Create your views here.
