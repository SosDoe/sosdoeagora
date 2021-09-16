from django.contrib import admin
from .models import Doador, Instituicao, Produto, Doacao, Beneficiario

admin.site.register(Doador)
admin.site.register(Instituicao)
admin.site.register(Produto)
admin.site.register(Doacao)
admin.site.register(Beneficiario)

