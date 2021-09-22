from django.urls import path
from . import views

app_name = 'doeagora'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('sobre-cadastros', views.SobreCadastrosView.as_view(), name='sobrecadastros'),
    path('sosdoeinformacoes', views.SosDoeInfoView.as_view(), name='sosdoeinfo'),  
    path('cadastro-beneficiarios', views.CadastroBeneficiariosView.as_view(), name='c.beneficiario'),  
    path('cadastro-doadores', views.CadastroDoadoresView.as_view(), name='c.doadores'),
    path('cadastro-instituição', views.CadastroInstituicaoView.as_view(), name='c.instituição'),
    path('fim-cadastro', views.FimParaBeneficiadosView.as_view(), name='fim_beneficiados'),
    path('ver-beneficiario/<int:pk>', views.VerBeneficiarioView.as_view(), name='ver_beneficiario'),
    path('ver-instituição/<int:pk>', views.VerInstituicaoView.as_view(), name='ver_instituição'),
    path('ver-doadores/<int:pk>', views.VerDoadorView.as_view(), name='ver_doadores'),
]
