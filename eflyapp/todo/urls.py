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
]