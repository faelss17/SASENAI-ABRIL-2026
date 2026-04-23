from rest_framework import serializers

from .models import Agendamento, Barbeiro, Cliente, Servico


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class BarbeiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barbeiro
        fields = '__all__'


class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = '__all__'


class AgendamentoSerializer(serializers.ModelSerializer):
    cliente_nome = serializers.CharField(source='cliente.nome', read_only=True)
    barbeiro_nome = serializers.CharField(source='barbeiro.nome', read_only=True)
    servico_nome = serializers.CharField(source='servico.nome', read_only=True)

    class Meta:
        model = Agendamento
        fields = [
            'id', 'cliente', 'cliente_nome', 'barbeiro', 'barbeiro_nome',
            'servico', 'servico_nome', 'data', 'horario', 'observacoes',
            'status', 'criado_em'
        ]
