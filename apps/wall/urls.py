from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('users/show/<int:id>', views.showUser),
    path('dashboard', views.dashboard),
    path('wish',views.wish)

]
