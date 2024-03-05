from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'panos'

urlpatterns = [
    path('', views.home, name='home'),
    path('panos_de_prato/categoria/<int:categoria_id>/', views.categoria, name='categoria'),
    path('panos_de_prato/<int:id>/', views.pano, name='pano'),
    path('panos_de_prato/procurar/', views.procurar, name='procurar'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
