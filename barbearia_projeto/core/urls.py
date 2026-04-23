from django.urls import path

from . import views

urlpatterns = [
    path('clientes/', views.ClienteListView.as_view(), name='cliente-list'),
    path('clientes/novo/', views.ClienteCreateView.as_view(), name='cliente-create'),
    path('clientes/<int:pk>/editar/', views.ClienteUpdateView.as_view(), name='cliente-update'),
    path('clientes/<int:pk>/excluir/', views.ClienteDeleteView.as_view(), name='cliente-delete'),

    path('barbeiros/', views.BarbeiroListView.as_view(), name='barbeiro-list'),
    path('barbeiros/novo/', views.BarbeiroCreateView.as_view(), name='barbeiro-create'),
    path('barbeiros/<int:pk>/editar/', views.BarbeiroUpdateView.as_view(), name='barbeiro-update'),
    path('barbeiros/<int:pk>/excluir/', views.BarbeiroDeleteView.as_view(), name='barbeiro-delete'),

    path('servicos/', views.ServicoListView.as_view(), name='servico-list'),
    path('servicos/novo/', views.ServicoCreateView.as_view(), name='servico-create'),
    path('servicos/<int:pk>/editar/', views.ServicoUpdateView.as_view(), name='servico-update'),
    path('servicos/<int:pk>/excluir/', views.ServicoDeleteView.as_view(), name='servico-delete'),

    path('agendamentos/', views.AgendamentoListView.as_view(), name='agendamento-list'),
    path('agendamentos/novo/', views.AgendamentoCreateView.as_view(), name='agendamento-create'),
    path('agendamentos/<int:pk>/editar/', views.AgendamentoUpdateView.as_view(), name='agendamento-update'),
    path('agendamentos/<int:pk>/excluir/', views.AgendamentoDeleteView.as_view(), name='agendamento-delete'),
]
