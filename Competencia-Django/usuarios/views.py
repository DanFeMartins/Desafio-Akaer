from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User  # Importe o modelo de usuário do Django
from . models import Empresa, Projeto
from .forms import EmpresaForm

def criar_usuario(request):
    if request.method == 'POST': #envio de dados
        # Obter os dados do front-end
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Cria um usuario novo com base nos dados do formulário
        novo_usuario = User.objects.create_user(username=username, password=password) 
        novo_usuario.save()

        # autenticação do usuario
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

        return redirect('listar_usuarios')  # Redirecionar para a página de lista de usuários após a criação
    else:
        return render(request, 'criar_usuario.html')


def atualizar_usuario(request, usuario_id):
    usuario = get_object_or_404(User, pk=usuario_id) #obtem o usuario pelo id

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # atualiza os detalhes do usuario
        usuario.username = username
        usuario.set_password(password)  # define a nova senha do usuário
        usuario.save() 

        return redirect('/usuario/listar_usuarios/')  # redireciona para a página de lista de usuários
    else:
        return render(request, 'atualizar_usuario.html', {'usuario': usuario})

    
def listar_usuarios(request):
    usuarios = User.objects.all() #lista todos os usuários presentes no banco de dados
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})


def deletar_usuario(request, usuario_id):
    usuario = get_object_or_404(User, pk=usuario_id)
    usuario.delete()
    return redirect('/usuario/listar_usuarios/')  # redireciona para a página de lista de usuários após a exclusão


#Empresas
def criar_empresa(request):
    if request.method == 'POST': #requisita dados do front-end
        form = EmpresaForm(request.POST) #cria um formulario do tipo EmpresaForm que contem nome  e usuarios
        if form.is_valid(): #verifica se o formulario é valido
            empresa = form.save(commit=False)
            empresa.save()  
            usuarios = form.cleaned_data['usuarios'] #adquire os usuarios do formulario
            empresa.usuarios.set(usuarios) #associa os usuarios a empresa, na tabela de relacionamento do bando de dados
            return redirect('/usuario/pagina_inicial/')
    else:
        form = EmpresaForm()
    return render(request, 'criar_empresa.html', {'form': form})



def listar_empresas_usuario(request):
    empresas = Empresa.objects.filter(usuarios=request.user) #lista todas as empresas presentes no banco de dados
    return render(request, 'pagina_inicial.html', {'empresas': empresas})


def delete_empresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, pk=empresa_id)
    usuario = get_object_or_404(User, pk=request.user.id)
    empresa.usuarios.remove(usuario)
    empresa.delete()
    return redirect('/usuario/pagina_inicial/')  # Redirecionar para a página de lista de usuários após a exclusão


def atualizar_empresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, pk=empresa_id)

    if request.method == 'POST':
        form = EmpresaForm(request.POST, instance=empresa) #cria um formulario do tipo EmpresaForm que contem nome  e usuarios
        if form.is_valid():
            empresa = form.save(commit=False) #salva os dados do formulario na variavel empresa, mas não no bando de dados
            empresa.save()
            usuarios = form.cleaned_data['usuarios'] #adquire os usuarios do formulario
            empresa.usuarios.set(usuarios) #associa os usuarios a empresa, na tabela de relacionamento do bando de dados
            return redirect('/usuario/pagina_inicial/')
    else:
        form = EmpresaForm(instance=empresa)
    return render(request, 'criar_empresa.html', {'form': form})


#Projetos
@login_required(login_url='/usuario/login/')
def criar_projeto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        
        # adiquire o usuario logado
        usuario = request.user
        
        # adiquire a empresa selecionada
        empresa_id = request.POST.get('empresa')
        empresa = Empresa.objects.get(id=empresa_id)
        
        # cria um novo projeto
        novo_projeto = Projeto.objects.create(nome=nome)
        
        # associa o usuário logado ao projeto
        novo_projeto.usuario.set([usuario])
        empresa.projetos.set([novo_projeto])
        
        novo_projeto.save()

        return redirect('listar_projetos')  
    else:
        return render(request, 'criar_projeto.html', {'empresas': Empresa.objects.all()})
    

def listar_projeto(request):
    projetos = Projeto.objects.filter(empresa__usuarios=request.user) #lista todos os projetos presentes no banco de dados
    return render(request, 'listar_projetos.html', {'projetos': projetos})


def deletar_projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, pk=projeto_id)
    projeto.delete()
    return redirect('/usuario/listar_projetos/')  # Redirecionar para a página de lista de projetos após a exclusão

def atualizar_projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, pk=projeto_id)
    empresas = Empresa.objects.all()

    if request.method == 'POST':
        # Obter os dados do formulário
        nome = request.POST.get('nome')

        # Atualizar os detalhes do projeto
        projeto.nome = nome
        projeto.save()

        empresa_id = request.POST.get('empresa')
        empresa = Empresa.objects.get(id=empresa_id)
        empresa.projetos.set([projeto])

        return redirect('/usuario/listar_projetos/')  # Redirecionar para a página de lista de projetos após a atualização
    else:
        return render(request, 'atualizar_projeto.html', {'projeto': projeto, 'empresas': empresas})