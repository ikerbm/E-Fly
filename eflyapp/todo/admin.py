from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Ciudad)
admin.site.register(Vuelo)
admin.site.register(Compra)
admin.site.register(Mensaje)
admin.site.register(Noticia)
admin.site.register(Ticket)
admin.site.register(Tarjeta)

'''class usuarioInline(admin.StackedInline):
    model = Usuario
    can_delete = False
    verbose_name  = 'Usuarios'

class CustomizedUserAdmin(UserAdmin):
    inlines = (usuarioInline, )


admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)'''