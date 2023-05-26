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
            return render(request,'todo/homeroot.html')
        #Pagina de inicio para el administrador
        elif (request.user.tipoUsuario == 'admin'): 
            return render(request,'todo/homeadministrador.html')
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
def AdministrarTarjetas(request,DNI):
    cliente = CustomUser.objects.get(DNI=DNI)
    tarjetas = Tarjeta.objects.filter(clienteid=cliente)
    context = {
        'cliente': cliente,
        'tarjetas': tarjetas,
    }
    return render(request,'todo/AdministrarTarjetas.html',context)

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
            filas = form.cleaned_data['filas']
            asientos_fila = form.cleaned_data['asientos_fila']
            print("entrando al for")
            for i in range(filas):
                for j in range(asientos_fila):
                    code = str(i % filas +1)+ chr(ord('A') + j % asientos_fila) 
                    print(code)
                    seat = Seat(vuelo=vuelo, estado = 'disponible', code = code)
                    seat.save()

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
def eliminar_tarjeta(request, tarjeta_id):
    tarjeta = Tarjeta.objects.get(id=tarjeta_id)
    tarjeta.delete()
    return redirect('home')

@login_required
def AddSaldo(request, DNI):
    cliente = CustomUser.objects.get(DNI=DNI)
    tarjetas = Tarjeta.objects.filter(clienteid=cliente)

    if request.method == 'POST':
        form = AddSaldoForm(request.POST)
        if form.is_valid():
            saldo = form.cleaned_data['saldo']
            cliente.saldo += saldo
            cliente.save()
            return redirect('home')
    else:
        if tarjetas.exists():
            form = AddSaldoForm()
        else:
            return redirect('AddCard.html')

    context = {
        'form': form,
        'cliente': cliente,
        'tarjetas': tarjetas,
    }
    return render(request, 'todo/AddSaldo.html', context)

@login_required
@user_passes_test(lambda u: u.tipoUsuario == 'cliente')
def comprar_vuelo(request, vuelo_id):
    vuelo = Vuelo.objects.get(id=vuelo_id)

    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            asientos_economica = form.cleaned_data['asientos_economica']
            asientos_primera = form.cleaned_data['asientos_primera']
            
            precio = (int(asientos_primera) * vuelo.precioPrimera) + (int(asientos_economica) * vuelo.precioEconomica)
            usuario = request.user

            compra = Compra(vuelo=vuelo, precio = precio, user_id = usuario.DNI, asientos_economica = asientos_economica, asientos_primera = asientos_primera)
            compra.save()

            return redirect('seleccionar_asiento', compra_id=compra.id)

    else:
        form = CompraForm(initial={'vuelo_id': vuelo_id})

    return render(request, 'todo/comprar_vuelo.html', {'form': form, 'vuelo': vuelo})

@login_required
@user_passes_test(lambda u: u.tipoUsuario == 'cliente')
def seleccionar_asiento(request, compra_id):
    compra = Compra.objects.get(id=compra_id)
    vuelo = Vuelo.objects.get(id=compra.vuelo_id)
    seats = Seat.objects.filter(vuelo=vuelo)
    filas_asientos = [[] for _ in range(vuelo.filas)]
    asientos_primera = compra.asientos_primera
    asientos_economica = compra.asientos_economica

    for seat in seats:
        codigo = seat.code
        numero_fila = int(codigo[:-1]) - 1  # Obtener el número de fila restando 1
        filas_asientos[numero_fila].append(seat)

    if request.method == 'POST':
        form = SeatSelectionForm(vuelo, request.POST)
        if form.is_valid():
            for seat in vuelo.seat_set.all():
                if (form.cleaned_data[f'seat_{seat.code}']): 
                    seat.estado = 'ocupado'
                    if(asientos_primera > 0):
                        clase = 'primera'
                        asientos_primera -= 1
                    elif(asientos_economica > 0):
                        clase = 'economica'
                        asientos_economica -= 1

                    ticket = Ticket(Compraid=compra,Vueloid=vuelo,asiento=seat,clase=clase)
                    ticket.save()

                seat.save()

            compra.estado = 'Reservada'
            compra.save()
            return redirect('ver_compras')

    else:
        form = SeatSelectionForm(vuelo)

    return render(request, 'todo/seleccionar_asiento.html', {'filas_asientos':  filas_asientos,'form': form,'compra': compra, 'vuelo': vuelo, 'seats':seats, 'filas': vuelo.filas, 'asientos_fila': vuelo.asientos_fila})

@login_required
@user_passes_test(lambda u: u.tipoUsuario == 'cliente')
def ver_compras(request):
    compras = Compra.objects.filter(user_id=request.user.DNI)
    tickets = Ticket.objects.filter(Compraid__user=request.user)

    # Configura el paginador con 10 elementos por página
    paginator = Paginator(compras, 10)

    # Obtiene el número de página de la consulta GET, si no se proporciona, usa el valor 1
    page_number = request.GET.get('page', 1)

    # Obtiene el objeto Page correspondiente a la página solicitada
    page = paginator.get_page(page_number)

    return render(request, 'todo/ver_compras.html', {'page': page, 'tickets': tickets})

@login_required
@user_passes_test(lambda u: u.tipoUsuario == 'cliente')
def cancelar_compra(request, compra_id):
    compra = get_object_or_404(Compra, id=compra_id)
    tickets = Ticket.objects.filter(Compraid=compra)

    # Cambiar el estado de las Seats relacionadas a los Tickets
    seat_codes = [ticket.asiento.code for ticket in tickets]
    seats_to_update = Seat.objects.filter(vuelo=compra.vuelo, code__in=seat_codes)
    seats_to_update.update(estado='disponible')
    
    if request.method == 'POST':
        compra.delete()
        return redirect('ver_compras')  # Reemplaza 'nombre_de_tu_ruta' con el nombre de la ruta a la que deseas redirigir después de borrar el vuelo
    
@login_required
@user_passes_test(lambda u: u.tipoUsuario == 'cliente')
def pagar_compra(request, compra_id):
    compra = get_object_or_404(Compra, id=compra_id)
    vuelo = Vuelo.objects.get(id=compra.vuelo_id)
    tickets = Ticket.objects.filter(Compraid=compra)

    # Cambiar el estado de las Seats relacionadas a los Tickets
    seat_codes = [ticket.asiento.code for ticket in tickets]
    seats = Seat.objects.filter(vuelo=compra.vuelo, code__in=seat_codes)


    return render(request, 'todo/pagar_compra.html', {'compra': compra, 'vuelo': vuelo, 'tickets': tickets, 'seats': seats,})

@login_required
@user_passes_test(lambda u: u.tipoUsuario == 'cliente')
def pay_compra(request, compra_id):
    compra = Compra.objects.get(id=compra_id)
    cliente = request.user

    cliente.saldo -= compra.precio
    cliente.save()

    compra.estado = 'Pagado'
    compra.save()


    return redirect('ver_compras')