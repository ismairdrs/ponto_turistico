from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracaoViewSet
from endereco.api.viewsets import EnderecoViewSet
from comentarios.api.viewsets import ComentarioViewSet
from avaliacoes.api.viewsets import AvaliacaoViewSet
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r'pontoturistico', PontoTuristicoViewSet, basename='PontoTuristico')
router.register(r'atracoes', AtracaoViewSet)
router.register(r'enderecos', EnderecoViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
