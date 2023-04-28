from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required


'''def home(request):
    usuarios = Usuario.objects.all()
    context = {'usuarios':usuarios}
    return render(request,'todo/home.html',context)

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateUserForm()

    context = {'form': form}     
    return render(request, 'todo/userRegister.html', context)'''


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LoginForm()

    context = {'form': form}     
    return render(request, 'todo/login.html', context)

