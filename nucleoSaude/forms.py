from django import forms
from .models import MensagemContato
from .models import Agendamento
from .models import Medicos
from .models import Pacientes
from .models import Prontuario
from django.contrib.auth.models import User

class CadastroMedicosModelForm(forms.ModelForm):
    
    class Meta:
        model = Medicos
        fields = ['nome_medico', 'crm', 'especialidade', 'telefone', 'email']
        widgets = {
            'nome_medico': forms.TextInput(attrs={'placeholder': 'nome_medico', 'class': 'form-control'}),
            'especialidade': forms.TextInput(attrs={'placeholder': 'especialidade', 'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'placeholder': 'telefone', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'seu-email@exemplo.com', 'class': 'form-control'}),
        }
        labels = {
            'nome_paciente': 'Nome Completo',
            'email': 'Seu E-mail',
        }

class CadastroPacientesModelForm(forms.ModelForm):
    
    class Meta:
        model = Pacientes
        fields = ['nome_paciente', 'numero_prontuario', 'data_nascimento', 'telefone', 'endereco', 'email']
        widgets = {
            'nome_paciente': forms.TextInput(attrs={'placeholder': 'nome_paciente', 'class': 'form-control'}),
            'numero_prontuario': forms.TextInput(attrs={'placeholder': 'numero_prontuario', 'class': 'form-control'}),
            'data_nsacimento': forms.DateInput(attrs={'placeholder': 'data_consulta', 'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'placeholder': 'telefone', 'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'placeholder': 'endereco', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'seu-email@exemplo.com', 'class': 'form-control'}),
        }
        labels = {
            'nome_paciente': 'Nome Completo',
            'prontuario': 'Número da caderneta',
            'email': 'Seu E-mail',
        }

class ContatoModelForm(forms.ModelForm):
    
    class Meta:
        model = MensagemContato
        fields = ['nome', 'email', 'assunto', 'mensagem']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Seu nome completo', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'seu-email@exemplo.com', 'class': 'form-control'}),
            'assunto': forms.TextInput(attrs={'placeholder': 'Assunto da mensagem', 'class': 'form-control'}),
            'mensagem': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Digite sua mensagem...', 'class': 'form-control'}),
        }
        labels = {
            'nome': 'Nome Completo',
            'email': 'Seu E-mail',
        }

class AgendamentoModelForm(forms.ModelForm):
    
    class Meta:
        model = Agendamento
        fields = ['nome_paciente', 'numero_prontuario', 'data_consulta', 'nome_medico']
        widgets = {
            'nome_paciente': forms.TextInput(attrs={'placeholder': 'nome_paciente', 'class': 'form-control'}),
            'numero_prontuario': forms.TextInput(attrs={'placeholder': 'numero_prontuario', 'class': 'form-control'}),
            'data_consulta': forms.DateInput(attrs={'placeholder': 'data_consulta', 'class': 'form-control'}),
            'nome_medico': forms.TextInput(attrs={'placeholder': 'nome_medico', 'class': 'form-control'}),
        }
        labels = {
            'nome_paciente': 'Nome Completo',
            'email': 'Seu E-mail',
        }

class ProntuarioModelForm(forms.ModelForm):
    
    class Meta:
        model = Prontuario
        fields = ['nome_paciente', 'numero_prontuario', 'prontuario_medico']
        widgets = {
            'nome_paciente': forms.TextInput(attrs={'placeholder': 'nome_paciente', 'class': 'form-control'}),
            'numero_prontuario': forms.TextInput(attrs={'placeholder': 'numero_prontuario', 'class': 'form-control'}),
            'prontuario_medico': forms.TextInput(attrs={'placeholder': 'prontuario_medico', 'class': 'form-control'}),
        }
        labels = {
            'nome_paciente': 'Nome Completo',
            'prontuario': 'Número da caderneta',
           
        }

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuário')
    password = forms.CharField(label='Senha',widget=forms.PasswordInput)

class RegistroForm(forms.ModelForm):
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme a senha',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','email')

    def clean(self):
        cleaned = super().clean()
        if cleaned.get('password') != cleaned.get('password2'):
            raise forms.ValidationError('Senhas diferentes')
        return cleaned