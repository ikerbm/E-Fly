from django.shortcuts import render,redirect,get_object_or_404

from django.contrib.auth.decorators import user_passes_test
from django.views.generic import ListView, DeleteView

from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,authenticate,login,update_session_auth_hash

from django.core.paginator import Paginator

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

#Pagina principal para cada tipo de usuario
def home(request):
    if request.user.is_authenticated:
        #El root esta de finido como is_staff en la base de datos
        #Pagina de inicio para el root
        if (request.user.is_staff): 
            return render(request,'todo/home.html')
        #Pagina de inicio para el administrador
        elif (request.user.tipoUsuario == 'admin'): 
            return render(request,'todo/home.html')
        else:
        #Pagina de inicio para el usuario normal
            return render(request,'todo/home.html')
    else:
        #Pagina de inicio para el visitante
        return render(request, 'todo/home.html')
    


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


@login_required
def AddCard(request,DNI):
    if request.method == 'POST':
        form = AddCardForm(request.POST)
        
        if form.is_valid(): 
            tarjeta = form.save(commit=False)
            tarjeta.clienteid = request.user
            tarjeta=form.save()
            return redirect('home')
    else:
        form = AddCardForm()

    context = {'form': form}     
    return render(request, 'todo/AddCard.html', context)

@login_required
@user_passes_test(lambda u: u.tipoUsuario == 'admin')
def crear_vuelo(request):
    if request.method == 'POST':
        form = CreateVueloForm(request.POST)
        if form.is_valid():
            vuelo = form.save()
            return redirect('ver_vuelos')
        else:
            errors = form.errors.as_data()
            for field, error in errors.items():
                field_value = form.cleaned_data.get(field)
                print(f"Error en {field}: {error[0].message} (Valor: {field_value})")
    else:
        form = CreateVueloForm()
    return render(request, 'todo/create_vuelo.html', {'form': form, 'errors': form.errors})


def ver_vuelos(request):
    vuelos = Vuelo.objects.all()

    filtro_form = FiltroVuelosForm(request.GET)

    destino = request.GET.get('destino')
    origen = request.GET.get('origen')
    fecha_salida = request.GET.get('fecha_salida')

    if destino:
        vuelos = vuelos.filter(destino=destino)
    if origen:
        vuelos = vuelos.filter(origen=origen)
    if fecha_salida:
        vuelos = vuelos.filter(fechaSalida=fecha_salida)

    # Configura el paginador con 10 elementos por página
    paginator = Paginator(vuelos, 10)

    # Obtiene el número de página de la consulta GET, si no se proporciona, usa el valor 1
    page_number = request.GET.get('page', 1)

    # Obtiene el objeto Page correspondiente a la página solicitada
    page = paginator.get_page(page_number)

    return render(request, 'todo/ver_vuelos.html', {'page': page, 'filtro_form': filtro_form})

@login_required
@user_passes_test(lambda u: u.tipoUsuario == 'admin')
def borrar_vuelo(request, vuelo_id):
    vuelo = get_object_or_404(Vuelo, id=vuelo_id)
    
    if request.method == 'POST':
        vuelo.delete()
        return redirect('ver_vuelos')  # Reemplaza 'nombre_de_tu_ruta' con el nombre de la ruta a la que deseas redirigir después de borrar el vuelo
    
@login_required
@user_passes_test(lambda u: u.tipoUsuario == 'admin')
def edit_vuelo(request, vuelo_id):
    vuelo = get_object_or_404(Vuelo, id=vuelo_id)

    if request.method == 'POST':
        form = EditVueloForm(request.POST, instance=vuelo)
        if form.is_valid():
            form.save()
            return redirect('ver_vuelos')  # Redirige a la página deseada después de editar el vuelo
    else:
        form = EditVueloForm(instance=vuelo)

    return render(request, 'todo/edit_vuelo.html', {'form': form, 'vuelo': vuelo, 'errors': form.errors})

@login_required
@user_passes_test(lambda u: u.tipoUsuario == 'admin')
def promo_vuelo(request, vuelo_id):
    vuelo = get_object_or_404(Vuelo, id=vuelo_id)

    if request.method == 'POST':
        form = PromoVueloForm(request.POST, instance=vuelo)
        if form.is_valid():
            form.save()
            return redirect('ver_vuelos')  # Redirige a la página deseada después de editar el vuelo
    else:
        form = PromoVueloForm(instance=vuelo)

    return render(request, 'todo/promo_vuelo.html', {'form': form, 'vuelo': vuelo, 'errors': form.errors})