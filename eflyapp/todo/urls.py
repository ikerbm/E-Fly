from django.urls import path
from . import views
urlpatterns=[
    path("",views.home,name="home"),
    path('register/', views.register, name='register'),
    path('ChangePassword/', views.ChangePassword, name='ChangePassword'),
    path("Edit/<int:DNI>", views.Edit, name='Edit'),
    path('logout/',views.exit,name='exit'),
    path('create_admin/', views.create_admin, name='create_admin'),
    path('users/', views.user_list, name='user_list'),
    path('users/<int:pk>/delete/', views.UserDeleteView.as_view(), name='user_delete'),
    path("AdministrarTarjetas/<int:DNI>",views.AdministrarTarjetas,name="AdministrarTarjetas"),
    path("AddCard/<int:DNI>", views.AddCard, name='AddCard'),
    path('vuelo/create', views.crear_vuelo, name='crear_vuelo'),
    path('vuelo/', views.ver_vuelos, name='ver_vuelos'),
    path('vuelo/<int:vuelo_id>/delete/', views.borrar_vuelo, name='borrar_vuelo'),
    path('vuelo/<int:vuelo_id>/edit/', views.edit_vuelo, name='edit_vuelo'),
    path('vuelo/<int:vuelo_id>/promo/', views.promo_vuelo, name='promo_vuelo'),
    #path('crearvuelo/', views.crearvuelo, name='crearvuelo')
    path("AdministrarTarjetas/<int:DNI>/AddSaldo/", views.AddSaldo, name='AddSaldo'),
    path("administrarcompras/<int:DNI>",views.administrarcompras,name="administrarcompras"),
]