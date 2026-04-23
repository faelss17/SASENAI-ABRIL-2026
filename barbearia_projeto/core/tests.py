from datetime import time, timedelta

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APIClient

from .models import Agendamento, Barbeiro, Cliente, Servico


class ProtectedViewsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='123456Teste!')

    def test_dashboard_requires_login(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)

    def test_clientes_requires_login(self):
        response = self.client.get(reverse('cliente-list'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)

    def test_dashboard_logged_user_can_access(self):
        self.client.login(username='admin', password='123456Teste!')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)


class AgendamentoModelTests(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(
            nome='Carlos', telefone='31999999999', email='carlos@email.com'
        )
        self.barbeiro = Barbeiro.objects.create(
            nome='João', especialidade='Degradê', telefone='31988888888', ativo=True
        )
        self.servico = Servico.objects.create(
            nome='Corte', descricao='Corte tradicional', preco='35.00', duracao_estimada=45
        )

    def test_nao_permite_horario_duplicado_para_mesmo_barbeiro(self):
        data_futura = timezone.localdate() + timedelta(days=1)
        Agendamento.objects.create(
            cliente=self.cliente,
            barbeiro=self.barbeiro,
            servico=self.servico,
            data=data_futura,
            horario=time(14, 0),
        )

        with self.assertRaises(ValidationError):
            segundo = Agendamento(
                cliente=self.cliente,
                barbeiro=self.barbeiro,
                servico=self.servico,
                data=data_futura,
                horario=time(14, 0),
            )
            segundo.full_clean()
            segundo.save()


class ApiTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='123456Teste!')
        self.api_client = APIClient()
        self.cliente = Cliente.objects.create(
            nome='Marcos', telefone='31997777777', email='marcos@email.com'
        )

    def test_api_requires_authentication(self):
        response = self.api_client.get('/api/clientes/')
        self.assertIn(response.status_code, [401, 403])

    def test_api_cliente_list_authenticated(self):
        self.api_client.login(username='admin', password='123456Teste!')
        response = self.api_client.get('/api/clientes/')
        self.assertEqual(response.status_code, 200)

    def test_api_cliente_detail_not_found(self):
        self.api_client.login(username='admin', password='123456Teste!')
        response = self.api_client.get('/api/clientes/999/')
        self.assertEqual(response.status_code, 404)
