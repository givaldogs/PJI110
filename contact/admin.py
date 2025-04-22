from django.contrib import admin
from contact import models
from .models import StatusSolicitacao, SecretariaEmail, AssuntoReclamacao



# Register your models here.

@admin.register(StatusSolicitacao)
class StatusSolicitacaoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao']


@admin.register(AssuntoReclamacao)
class AssuntoReclamacaoAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']
    filter_horizontal = ['emails_secretaria']  # Interface melhor para selecionar vários
    

@admin.register(SecretariaEmail)
class SecretariaEmailAdmin(admin.ModelAdmin):
    list_display = ['nome_secretaria', 'email']
    search_fields = ['nome_secretaria', 'email']

