from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='panos-home'),
    path('panos_de_prato/<int:id>/', views.pano, name='panos-pano'),
]
