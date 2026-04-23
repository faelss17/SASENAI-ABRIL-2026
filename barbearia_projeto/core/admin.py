from django.contrib import admin

from .models import Agendamento, Barbeiro, Cliente, Servico


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email', 'data_cadastro')
    search_fields = ('nome', 'email', 'telefone')


@admin.register(Barbeiro)
class BarbeiroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'especialidade', 'telefone', 'ativo')
    list_filter = ('ativo',)
    search_fields = ('nome', 'especialidade')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'duracao_estimada')
    search_fields = ('nome',)


@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'barbeiro', 'servico', 'data', 'horario', 'status')
    list_filter = ('status', 'data', 'barbeiro')
    search_fields = ('cliente__nome', 'barbeiro__nome', 'servico__nome')
