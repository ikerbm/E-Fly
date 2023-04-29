from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required


def home(request):
    usuarios=Usuario.objects.all()
    context={'usuarios':usuarios}
    return render(request,'todo/home.html',context)

def register(request):
    if request.method == 'POST':
        form = CreateUsuarioForm(request.POST)
        
        if form.is_valid(): 
            form.save()
            return redirect('home')
    else:
        form = CreateUsuarioForm()

    context = {'form': form}     
    return render(request, 'todo/userRegister.html', context)



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

def ChangePassword(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        
        if form.is_valid(): 
            form.save()
            return redirect('home')
    else:
        form = ChangePasswordForm()

    context = {'form': form}     
    return render(request, 'todo/changePassword.html', context)

def Edit(request):
    if request.method == 'POST':
        form = EditForm(request.POST)
        
        if form.is_valid(): 
            form.save()
            return redirect('home')
    else:
        form = EditForm()

    context = {'form': form}     
    return render(request, 'todo/Edit.html', context)

