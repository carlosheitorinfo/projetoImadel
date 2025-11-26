from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('agenda/',views.Agenda, name='agenda'),
    path('agendar/',views.formulario_agendamento_view, name='agendar'),
    path('sucesso/', views.agendamento_sucesso_view, name='agendamento_sucesso'),
    path('pacientes/',views.Pacientes, name='pacientes'),
    path('contato/', views.formulario_contato_view, name='contatos'),
    path('contato/sucesso/', views.contato_sucesso_view, name='contato_sucesso'),
    path('login/', views.login_view, name='login'),
    path('logout/',views.logout_view ,name='logout'),
    path('perfil/',views.perfil ,name='perfil'),
    path('registrar/',views.registrar_view ,name='registrar'),
]