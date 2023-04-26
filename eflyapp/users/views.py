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
    return render(request, 'userRegister.html', context)

def login(request):
    context = {'variable': 'valor'}
    return render(request, 'login.html', context)

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World")