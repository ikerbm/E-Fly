# Generated by Django 4.2.1 on 2025-01-28 17:10

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('DNI', models.IntegerField(default=0, primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(9999999999)])),
                ('saldo', models.IntegerField(default=0)),
                ('fechaNaci', models.DateField(null=True)),
                ('dirFact', models.CharField(max_length=100, null=True)),
                ('sexo', models.CharField(choices=[('H', 'Hombre'), ('M', 'Mujer'), ('N', 'No Responde')], default='N', max_length=20)),
                ('tipoUsuario', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('picture', models.ImageField(default='profile_default.png', upload_to='users/')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCiudad', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=100)),
                ('hora', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asientos_economica', models.IntegerField(default=10)),
                ('asientos_primera', models.IntegerField(default=10)),
                ('precio', models.IntegerField(default=10)),
                ('fecha', models.DateField(auto_now=True)),
                ('estado', models.CharField(default='sin_selec', max_length=16, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now=True)),
                ('texto', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=4)),
                ('estado', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Vuelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, null=True, unique=True)),
                ('origen', models.CharField(choices=[('Pereira', 'Pereira'), ('Bogotá', 'Bogotá'), ('Medellín', 'Medellín'), ('Cali', 'Cali'), ('Cartagena', 'Cartagena'), ('Madrid', 'Madrid'), ('Londres', 'Londres'), ('New York', 'New York'), ('Buenos Aires', 'Buenos Aires'), ('Miami', 'Miami')], max_length=100)),
                ('destino', models.CharField(choices=[('Pereira', 'Pereira'), ('Bogotá', 'Bogotá'), ('Medellín', 'Medellín'), ('Cali', 'Cali'), ('Cartagena', 'Cartagena'), ('Madrid', 'Madrid'), ('Londres', 'Londres'), ('New York', 'New York'), ('Buenos Aires', 'Buenos Aires'), ('Miami', 'Miami')], max_length=100)),
                ('filas', models.IntegerField(default=0)),
                ('asientos_fila', models.IntegerField(default=0)),
                ('precioPrimera', models.IntegerField()),
                ('precioEconomica', models.IntegerField()),
                ('precioPrimeraDesc', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('precioEconomicaDesc', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('fechaSalida', models.CharField(max_length=20, null=True)),
                ('horaSalida', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(23)])),
                ('minutoSalida', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(59)])),
                ('fechaLlegada', models.CharField(max_length=20, null=True)),
                ('horaLlegada', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(23)])),
                ('minutoLlegada', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(59)])),
                ('tiempoVuelo', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePasajero', models.CharField(max_length=50, null=True)),
                ('emailPasajero', models.EmailField(max_length=254, null=True)),
                ('edadPasajero', models.IntegerField(null=True)),
                ('clase', models.CharField(choices=[('p', 'Primera Clase'), ('e', 'Clase Economica')], max_length=20)),
                ('EstadoCheckIn', models.CharField(default='No Realizado', max_length=15)),
                ('Compraid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compraid', to='todo.compra')),
                ('Vueloid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vueloid', to='todo.vuelo')),
                ('asiento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todo.seat')),
            ],
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('d', 'debito'), ('c', 'credito')], max_length=16)),
                ('disponible', models.IntegerField(default=200000)),
                ('numero', models.CharField(max_length=16)),
                ('nombre', models.CharField(max_length=16)),
                ('cvv', models.CharField(max_length=3)),
                ('vencimiento', models.DateField()),
                ('clienteid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='seat',
            name='vuelo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todo.vuelo'),
        ),
        migrations.AddField(
            model_name='compra',
            name='vuelo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todo.vuelo'),
        ),
    ]
