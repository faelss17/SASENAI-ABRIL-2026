from datetime import datetime

from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Cliente(models.Model):
    nome = models.CharField(max_length=120)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome


class Barbeiro(models.Model):
    nome = models.CharField(max_length=120)
    especialidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Barbeiro'
        verbose_name_plural = 'Barbeiros'

    def __str__(self):
        return self.nome


class Servico(models.Model):
    nome = models.CharField(max_length=120)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    duracao_estimada = models.PositiveIntegerField(help_text='Duração em minutos')

    class Meta:
        ordering = ['nome']
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return f'{self.nome} - R$ {self.preco}'


class Agendamento(models.Model):
    STATUS_CHOICES = [
        ('agendado', 'Agendado'),
        ('concluido', 'Concluído'),
        ('cancelado', 'Cancelado'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='agendamentos')
    barbeiro = models.ForeignKey(Barbeiro, on_delete=models.PROTECT, related_name='agendamentos')
    servico = models.ForeignKey(Servico, on_delete=models.PROTECT, related_name='agendamentos')
    data = models.DateField()
    horario = models.TimeField()
    observacoes = models.TextField(blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='agendado')
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['data', 'horario']
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'
        constraints = [
            models.UniqueConstraint(
                fields=['barbeiro', 'data', 'horario'],
                name='unique_horario_por_barbeiro'
            )
        ]

    def __str__(self):
        return f'{self.cliente} - {self.servico} em {self.data} às {self.horario}'

    def clean(self):
        super().clean()

        if self.barbeiro and not self.barbeiro.ativo:
            raise ValidationError({'barbeiro': 'Não é possível agendar com um barbeiro inativo.'})

        if self.data and self.horario:
            data_hora = timezone.make_aware(datetime.combine(self.data, self.horario))
            if data_hora < timezone.localtime():
                raise ValidationError({'horario': 'Não é permitido criar agendamentos no passado.'})

        conflito = Agendamento.objects.filter(
            barbeiro=self.barbeiro,
            data=self.data,
            horario=self.horario,
        ).exclude(pk=self.pk)

        if self.barbeiro and self.data and self.horario and conflito.exists():
            raise ValidationError({'horario': 'Este barbeiro já possui um atendimento nesse horário.'})
