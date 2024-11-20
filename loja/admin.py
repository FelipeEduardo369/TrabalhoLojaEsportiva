from django.contrib import admin
from .models import Produto, Cliente, Fornecedor, Funcionario, NotaFiscal

admin.site.register(Produto)
admin.site.register(Cliente)
admin.site.register(Fornecedor)
admin.site.register(Funcionario)
admin.site.register(NotaFiscal)
