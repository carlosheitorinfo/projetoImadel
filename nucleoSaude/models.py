from django.db import models
from django.utils import timezone

# Create your models here.

class Medicos(models.Model):
    nome_medico = models.CharField(max_length=100)
    crm = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    ativo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Médico"
        verbose_name_plural = "Médicos" 
    def __str__(self):
        return self.nome_medico
    
class Pacientes(models.Model):
    numero_prontuario = models.PositiveIntegerField(unique=True, primary_key=True)
    nome_paciente = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes" 
    
    def __str__(self):
        return self.nome_paciente

class Agendamento(models.Model):
    nome_paciente = models.CharField(max_length=100)
    numero_prontuario = models.ForeignKey(Pacientes)
    data_consulta = models.DateField(max_length=100)
    nome_medico = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"consulta de {self.nome_paciente}, pronuário {self.numero_prontuario} em {self.data_consulta}, com Dr.(a) {self.nome_medico}"

class Agenda(models.Model):
    nome_paciente = models.CharField(max_length=100)
    numero_prontuario = models.PositiveIntegerField()
    data_consulta = models.DateField(max_length=100)
    nome_medico = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)
   
    def __str__(self):
        return f"consulta de {self.nome_paciente}, pronuário {self.numero_prontuario} em {self.data_consulta}, com Dr.(a) {self.nome_medico}"

class Prontuario(models.Model):
    nome_paciente = models.CharField(max_length=100)
    numero_prontuario = models.PositiveIntegerField()
    prontuario_medico = models.TextField()
    
    class Meta:
        verbose_name = "Prontuario"
        verbose_name_plural = "Prontuarios"
    
    def __str__(self):
        return f"Prontuario medico de {self.nome_paciente}, pronuário {self.prontuario_medico} "

class MensagemContato(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    assunto = models.CharField(max_length=200)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(default=timezone.now)
    lido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.assunto} - {self.nome} ({self.email})"

    class Meta:
        verbose_name = "Mensagem de Contato"
        verbose_name_plural = "Mensagens de Contato"
        ordering = ['-data_envio']