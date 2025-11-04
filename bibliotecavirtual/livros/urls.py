
from django.urls import path
from .import views





urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_usuario, name='login'),
    path('livros/', views.listar_livros, name='listar_livros'),
    path('livros/novo', views.cadastrar_livros, name='cadastrar_livros'),
    path('usuario/', views.cadastrar_usuario, name ='cadastrar_usuario'),
    path('dashboard/', views.dashboard, name ='dashboard'),
    path('logout', views.sair, name='logout'),
    path('realizar_emprestimo/', views.emprestar_livros, name='emprestar'),
    path('livros_devolvido/devover/<int:pk>', views.devolver_livro, name='devolver'),
    path('livros_emprestados/', views.listar_livros_emprestado, name='emprestar_livros'),
    path('edita/<int:pk>/', views.editar_livros, name='editar'),
    path('livros/remover/<int:pk>/', views.apagar_livro, name='apagar_livro'),
    path('emprestimos/remover/<int:pk>/', views.remover_emprestimo, name='remover_emprestimo'),
    path('livros/pesquisar/', views.pesquisar, name='pesquisar'),


]
