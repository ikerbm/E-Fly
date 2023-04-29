from django.urls import path
from . import views
urlpatterns=[
    path("",views.home,name="home"),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('ChangePassword/', views.ChangePassword, name='ChangePassword'),
    path('Edit/', views.Edit, name='Edit'),
]