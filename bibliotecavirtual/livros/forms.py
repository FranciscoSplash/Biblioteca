from django import forms
from .models import Livros, Emprestimo, Usuario
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class FormularioCadastro(UserCreationForm):
    email = forms.EmailField(required=True)
   

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


        def __init__(self, *args, **kwargs):
               super(FormularioCadastro, self).__init__(*args, **kwargs)
               # Adicionando as mensagens de erro personalizadas para a senha
               self.fields['password1'].help_text =(
                       "Sua senha não pode ser muito semelhante a outras informações pessoais. "
                        "Sua senha deve ter pelo menos 8 caracteres. "
                         "Sua senha não pode ser uma senha comumente usada. "
                        "Sua senha não pode ser totalmente numérica."
               )

        
class LivrosForm(forms.ModelForm):
        class Meta:
                model = Livros
                fields = '__all__'

class UsuarioForm(forms.ModelForm):
        class Meta:
                model = Usuario
                fields = '__all__'


class EmprestimoForm(forms.ModelForm):
        class Meta:
                model = Emprestimo
                fields = ['livro', 'nome', 'telefone', 
                          'email', 'data_de_devolucao', 
                           'usuario']