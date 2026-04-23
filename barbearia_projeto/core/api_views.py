from rest_framework import permissions, viewsets

from .models import Agendamento, Barbeiro, Cliente, Servico
from .serializers import (
    AgendamentoSerializer,
    BarbeiroSerializer,
    ClienteSerializer,
    ServicoSerializer,
)


class AuthenticatedModelViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]


class ClienteViewSet(AuthenticatedModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class BarbeiroViewSet(AuthenticatedModelViewSet):
    queryset = Barbeiro.objects.all()
    serializer_class = BarbeiroSerializer


class ServicoViewSet(AuthenticatedModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer


class AgendamentoViewSet(AuthenticatedModelViewSet):
    queryset = Agendamento.objects.select_related('cliente', 'barbeiro', 'servico').all()
    serializer_class = AgendamentoSerializer
