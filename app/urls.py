from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.userLogin, name='login'),
    path('logout/', views.userLogout, name='logout'),
    path('register/', views.registerUser, name='register'),

    path('', views.index, name='index'),
    path('photo/<str:id>', views.viewPic, name='photo'),
    path('add/', views.add, name='add')
]
