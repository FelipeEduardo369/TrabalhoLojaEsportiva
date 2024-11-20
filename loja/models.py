from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField()
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=15)
    endereco = models.TextField()

    def __str__(self):
        return self.nome


class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    endereco = models.TextField()

    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    salario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome


class NotaFiscal(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_emissao = models.DateTimeField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    produtos = models.ManyToManyField(Produto)
    numero_nota = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"Nota {self.numero_nota} - Cliente: {self.cliente.nome}"
