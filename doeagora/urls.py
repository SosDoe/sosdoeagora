from django.urls import path
from . import views

app_name = 'doeagora'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('sobre-cadastros', views.SobreCadastrosView.as_view(), name='sobrecadastros'),
    path('sosdoeinformacoes', views.SosDoeInfoView.as_view(), name='sosdoeinfo'),  
    path('cadastro-beneficiarios', views.CadastroBeneficiariosView.as_view(), name='c.beneficiario'),  
    path('cadastro-doadores', views.CadastroDoadoresView.as_view(), name='c.doadores'),
    path('cadastro-instituicao', views.CadastroInstituicaoView.as_view(), name='c.instituicao'),
    path('interesse', views.CadastroInteresseView.as_view(), name='interesse'),
    path('cadastro-doacaobeneficiario', views.CadastroDoacaoBeneficiarioView.as_view(), name='doacaobeneficiario'),
    path('fim-cadastro', views.FimParaBeneficiadosView.as_view(), name='fim_beneficiados'),
    path('ver-doacao/<int:pk>', views.VerDoacaoView.as_view(), name='ver_doacao'),
    path('ver-beneficiario/<int:pk>', views.VerBeneficiarioView.as_view(), name='ver_beneficiario'),
    path('ver-instituicao/<int:pk>', views.VerInstituicaoView.as_view(), name='ver_instituicao'),
    path('ver-doadores/<int:pk>', views.VerDoadorView.as_view(), name='ver_doador'),
    path('ver-interesse/<int:pk>', views.VerInteresseView.as_view(), name='ver_interesse'),
    path('ver-doacaobeneficiario/<int:pk>', views.VerDoacaoBeneficiarioView.as_view(), name='ver_doacao_beneficiario'),
    path('doacao', views.DoacaoView.as_view(), name='doacao'),
    path('listagem', views.ListagemView.as_view(), name='listagem'),
    path('listagem-doacao', views.VerListagemDoacaoView.as_view(), name='verlistagemdoacao'),
    path('listagem-doadores', views.VerListagemDoadorView.as_view(), name='verlistagemdoador'),
    path('listagem-beneficiarios', views.VerListagemBeneficiarioView.as_view(), name='verlistagembeneficiario'),
    path('listagem-instituicoes', views.VerListagemInstituicaoView.as_view(), name='verlistageminstituicao'),
    path('listagem-interesse', views.VerListagemInteresseView.as_view(), name='verlistageminteresses'),
    path('listagem-doacaobeneficiario', views.VerListagemDoacaoBeneficiarioView.as_view(), name='verlistagemdoacaobeneficiario'),
    path('editar-beneficiario/<int:pk>/', views.EditarBeneficiarioView.as_view(), name='editar_beneficiario'),
    path('editar-doacao/<int:pk>/', views.EditarDoacaoView.as_view(), name='editar_doacao'),
    path('editar-instituicao/<int:pk>/', views.EditarInstituicaoView.as_view(), name='editar_instituicao'),
    path('editar-doadores/<int:pk>/', views.EditarDoadorView.as_view(), name='editar_doador'),
    path('editar-interesse/<int:pk>/', views.EditarInteresseView.as_view(), name='editar_interesse'),
    path('editar-doadorbeneficiario/<int:pk>/', views.EditarDoacaoBeneficiarioView.as_view(), name='editar_doacao_beneficiario'),
    path('excluir-beneficiario/<int:pk>/', views.ExcluirBeneficiarioView.as_view(), name='excluir_beneficiario'),
    path('excluir-instituicao/<int:pk>/', views.ExcluirInstituicaoView.as_view(), name='excluir_instituicao'),
    path('excluir-doacao/<int:pk>/', views.ExcluirDoacaoView.as_view(), name='excluir_doacao'),
    path('excluir-doadores/<int:pk>/', views.ExcluirDoadorView.as_view(), name='excluir_doador'),
    path('excluir-interesse/<int:pk>/', views.ExcluirInteresseView.as_view(), name='excluir_interesse'),
    path('excluir-doacaobeneficiario/<int:pk>/', views.ExcluirDoacaoBeneficiarioView.as_view(), name='excluir_doacao_beneficiario'),
    
    
]
