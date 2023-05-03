from django.shortcuts import render,redirect,get_object_or_404

from django.contrib.auth.decorators import user_passes_test
from django.views.generic import ListView, DeleteView

from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,authenticate,login,update_session_auth_hash

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

def home(request):
    return render(request,'todo/home.html')

def register(request):
    if request.method == 'POST':
        form = CreateUsuarioForm(request.POST)
        
        if form.is_valid(): 
            form.save()
            return redirect('home')
        else:
            errors = form.errors.as_data()
            for field, error in errors.items():
                print(f"Error en {field}: {error[0].message}")
    else:
        form = CreateUsuarioForm()

    context = {'form': form}     
    if form.errors:
        context['errors'] = form.errors
    return render(request, 'todo/userRegister.html', context)

@login_required
def ChangePassword(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user,request.POST)
        
        if form.is_valid(): 
            user=form.save()
            update_session_auth_hash(request,user)
            return redirect('home')
    else:
        form = ChangePasswordForm(request.user)

    context = {'form': form}     
    return render(request, 'todo/changePassword.html', context)

@login_required
def Edit(request,DNI):
    perfil=CustomUser.objects.get(DNI=DNI)

    if request.method == 'POST':
        form = EditForm(request.POST, instance=perfil)
        
        if form.is_valid(): 
            form.save()
            return redirect('home')
        else:
            errors = form.errors.as_data()
            for field, error in errors.items():
                print(f"Error en {field}: {error[0].message}")
    else:
        form = EditForm(instance=request.user)

    context = {'form': form}     
    return render(request, 'todo/Edit.html', context)

def exit(request):
    logout(request)
    return redirect('home')


#Ver Lista de Usuarios desde Root
@login_required
@user_passes_test(lambda u: u.is_superuser)
def user_list(request):
    users = User.objects.filter(tipoUsuario='admin')
    return render(request, 'todo/user_list.html', {'users': users})

class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('user_list')


@login_required
@user_passes_test(lambda u: u.is_superuser)
def create_admin(request):
    if request.method == 'POST':
        form = CreateAdminForm(request.POST)
        
        if form.is_valid(): 
            form.save()
            return redirect('user_list')
        else:
            errors = form.errors.as_data()
            for field, error in errors.items():
                print(f"Error en {field}: {error[0].message}")
    else:
        form = CreateAdminForm()

    context = {'form': form}   
    if form.errors:
        context['errors'] = form.errors  
    return render(request, 'todo/create_admin.html', context)