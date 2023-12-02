from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'agendamento'

router = routers.DefaultRouter()
router.register('', views.agendamentoViewSet, basename='agendamento')
router.register('', views.agendamentoalunoViewSet, basename='agendamentoaluno')
router.register('', views.agendamentoinstrutorViewSet, basename='agendamentoinstrutor')

urlpatterns = [
    path('', include(router.urls) )
]
