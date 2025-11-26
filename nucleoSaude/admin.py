from django.contrib import admin
from .models import Medicos, Pacientes, Agendamento, MensagemContato

# Register your models here.

@admin.register(Medicos)
class MedicosAdmin(admin.ModelAdmin):
    list_display = ('nome_medico', 'crm', 'especialidade', 'telefone','email')
    search_fields = ("nome_medico",)
    list_filter = ('nome_medico', 'especialidade')

@admin.register(Pacientes)
class PacientesAdmin(admin.ModelAdmin):
    list_display = ('nome_paciente', 'numero_prontuario', 'data_nascimento', 'telefone', 'endereco', 'email')
    list_filter = ('nome_paciente', 'numero_prontuario', 'data_nascimento')
    search_fields = ('nome_paciente', 'numero_prontuario', 'data_nascimento')

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('nome_paciente', 'numero_prontuario', 'data_consulta', 'nome_medico')
    list_filter = ('nome_paciente', 'numero_prontuario', 'data_consulta', 'nome_medico')
    search_fields = ('nome_paciente', 'numero_prontuario', 'data_consulta', 'nome_medico')

@admin.register(MensagemContato)
class MensagemContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'assunto', 'data_envio', 'lido')
    list_filter = ('lido', 'data_envio')
    search_fields = ('nome', 'email', 'assunto')