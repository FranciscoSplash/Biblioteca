from django.shortcuts import render, redirect
from .models import Livros, Usuario, Emprestimo
from .forms import LivrosForm, UsuarioForm, EmprestimoForm, FormularioCadastro
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.db.models import Q


# Create your views here.

# Redireciona para o login se não estiver autenticado
@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def home(request):
    return render(request, 'pages/home.html')


def cadastrar_usuario(request):

    if request.method =='POST':
        form = FormularioCadastro(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('login')
    else:
        form = FormularioCadastro()
    return render (request, 'pages/cadastro_usuario.html', {'form': form})


def login_usuario(request):
    if request.method == 'POST':
        username=request.POST['username']
        password =request.POST['password']
        usuario =authenticate(request, username =username, password =password)

        if usuario is not None:
            login(request, usuario)
            
            return redirect('home')    # redireciona para a view do painel
        else:
            messages.error(request, 'Usuário ou senha inválidos')
        


   
    return render(request, 'pages/login.html')

@login_required
def cadastrar_livros(request):
    if request.method=='POST':
        form =LivrosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro do livro realizado com sucesso!')
            return redirect('listar_livros')
    else:
        form =LivrosForm()

    return render(request, 'pages/cadastrar.html', {'form': form})

@login_required
def pesquisar(request):
    query =request.GET.get('q')
    resultado = []

    if query:
        resultado = Livros.objects.filter(
        Q(titulo__icontains =query)|Q(autor__icontains =query)
        )
    return render(request, 'pages/pesquisar.html',{'resultado':resultado, 'query': query})


@login_required
def editar_livros(request, pk):
    livro=get_object_or_404(Livros, pk=pk)
    if request.method =='POST':
        form =LivrosForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('listar_livros')
    else:
        form =LivrosForm(instance=livro)
    return render(request, 'pages/editar.html', {'form': form})

@login_required
def apagar_livro(request, pk):
    livro =get_object_or_404(Livros, pk=pk)
    livro.delete()
    return redirect('listar_livros')

@login_required
def remover_emprestimo(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)
    if emprestimo.devolvido:
        emprestimo.delete()
    return redirect('emprestar_livros')

@login_required
def emprestar_livros(request):
    if request.method=='POST':
        form =EmprestimoForm(request.POST)
        if form.is_valid():
            emprestimo =form.save(commit=False)
            
        # Marcar o livro como indisponível
            emprestimo.livro.disponivel=False
            emprestimo.livro.save()
            emprestimo.save()
            return redirect('emprestar')

    else:
        form =EmprestimoForm()

    return render(request, 'pages/emprestimo.html', {'form': form})


@login_required
def listar_livros_emprestado(request):
    emprestimos = Emprestimo.objects.all().order_by('data_de_emprestimo')
    return render(request, 'pages/livros_emprestados.html', {'emprestimos': emprestimos})
            

@login_required
def listar_livros(request):
    livros=Livros.objects.all()
    return render (request, 'pages/listar.html', {'livros': livros})

@login_required
def devolver_livro(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)
    emprestimo.devolvido =True
    emprestimo.livro.disponivel=True
    emprestimo.livro.save()
    emprestimo.save()
    return redirect('listar_livros')


@login_required
def sair(request):
    logout(request)
    return redirect('logout')  # redireciona para a tela de login após sair
