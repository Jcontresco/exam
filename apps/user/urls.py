from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('login', views.login),
    path('update/<int:id>', views.update),
    path('logout', views.logout),
    path('create', views.createUser),
    path('wish', views.makeWish)

]