from django.urls import path
from . import views

app_name = 'doeagora'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('sobre-cadastros', views.SobreCadastrosView.as_view(), name='sobrecadastros'),
]
