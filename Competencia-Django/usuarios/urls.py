from django.urls import path
from . import views

urlpatterns = [
    #urls usuario
    path('criar_usuario/', views.criar_usuario, name='criar_usuario'),
    path('<int:usuario_id>/atualizar_usuario/', views.atualizar_usuario, name='atualizar_usuario'), #deve ser passado um id existente de usuario
    path('listar_usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('<int:usuario_id>/deletar_usuario/', views.deletar_usuario, name='deletar_usuario'), #deve ser passado o id existente para exclusão de um usuario
    
    #urls empresa
    path('pagina_inicial/', views.listar_empresas_usuario, name='empresas'),
    path('criar_empresa/', views.criar_empresa, name='criar_empresa'),
    path('<int:empresa_id>/deletar_empresa/', views.delete_empresa, name='deletar_empresa'), #deve ser passado o id existente para exclusão de uma empresa
    path('<int:empresa_id>/atualizar_empresa/', views.atualizar_empresa, name='atualizar_empresa'), #deve ser passado o id existente para atualização de uma empresa
    
    #urls de projeto
    path('criar_projeto/', views.criar_projeto, name='criar_projeto'),
    path('listar_projetos/', views.listar_projeto, name='listar_projetos'),
    path('<int:projeto_id>/atualizar_projeto/', views.atualizar_projeto, name='atualizar_projeto'), #deve ser passado o id existente para atualização de um projeto
    path('<int:projeto_id>/deletar_projeto/', views.deletar_projeto, name='deletar_projeto'), #deve ser passado o id existente para exclusão de um projeto
]

