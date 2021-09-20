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
    path('fim-para-beneficiados', views.FimParaBeneficiadosView.as_view(), name='fim p beneficiados'),
]
