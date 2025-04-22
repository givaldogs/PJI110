from django.db import models

# Create your models here.
#
'''
----
Nome       | Descrição                       |
-----------+----------------------------------
Pendente   | Aguardando análise              |
Em Análise | Em avaliação pela secretaria    |
Resolvido  | Problema resolvido              |
Descartado | Solicitação sem procedência     |
'''
# Cadastro da situacao da solicitacao: 
class StatusSolicitacao(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Status da Solicitação'
        verbose_name_plural = 'Status das Solicitações'
        ordering = ['nome']  # Ordenação alfabética opcional

    def __str__(self):
        return self.nome

# Cadastro de e-mails das secretarias da prefeitura
class SecretariaEmail(models.Model):
    nome_secretaria = models.CharField(max_length=255)
    email = models.EmailField()

    class Meta:
        verbose_name = "Email da Secretaria"
        verbose_name_plural = "Emails das Secretarias"

    def __str__(self):
        return f"{self.nome_secretaria} - {self.email}"

# Cadastro de assuntos (problemas do bairro)
class AssuntoReclamacao(models.Model):
    nome = models.CharField(max_length=255)
    emails_secretaria = models.ManyToManyField(SecretariaEmail)

    class Meta:
        verbose_name = "Assunto da Reclamação"
        verbose_name_plural = "Assuntos da Reclamação"

    def __str__(self):
        return self.nome

