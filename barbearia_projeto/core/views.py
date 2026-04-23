from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, TemplateView, UpdateView

from .forms import AgendamentoForm, BarbeiroForm, ClienteForm, ServicoForm
from .models import Agendamento, Barbeiro, Cliente, Servico


class SuccessMessageMixin:
    success_message = ''

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.success_message:
            messages.success(self.request, self.success_message)
        return response


class DeleteMessageMixin:
    success_message = ''

    def form_valid(self, form):
        if self.success_message:
            messages.success(self.request, self.success_message)
        return super().form_valid(form)


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_clientes'] = Cliente.objects.count()
        context['total_barbeiros'] = Barbeiro.objects.count()
        context['total_servicos'] = Servico.objects.count()
        context['total_agendamentos'] = Agendamento.objects.count()
        context['ultimos_agendamentos'] = Agendamento.objects.select_related(
            'cliente', 'barbeiro', 'servico'
        ).order_by('-data', '-horario')[:5]

        labels_status = dict(Agendamento.STATUS_CHOICES)
        context['agendamentos_por_status'] = [
            {
                'status': item['status'],
                'label': labels_status.get(item['status'], item['status']),
                'total': item['total'],
            }
            for item in Agendamento.objects.values('status').annotate(total=Count('id'))
        ]
        return context


class ProtectedListView(LoginRequiredMixin, ListView):
    paginate_by = 10


class ClienteListView(ProtectedListView):
    model = Cliente
    template_name = 'core/cliente_list.html'
    context_object_name = 'clientes'


class ClienteCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'core/form.html'
    success_url = reverse_lazy('cliente-list')
    success_message = 'Cliente cadastrado com sucesso.'


class ClienteUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'core/form.html'
    success_url = reverse_lazy('cliente-list')
    success_message = 'Cliente atualizado com sucesso.'


class ClienteDeleteView(LoginRequiredMixin, DeleteMessageMixin, DeleteView):
    model = Cliente
    template_name = 'core/confirm_delete.html'
    success_url = reverse_lazy('cliente-list')
    success_message = 'Cliente excluído com sucesso.'


class BarbeiroListView(ProtectedListView):
    model = Barbeiro
    template_name = 'core/barbeiro_list.html'
    context_object_name = 'barbeiros'


class BarbeiroCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Barbeiro
    form_class = BarbeiroForm
    template_name = 'core/form.html'
    success_url = reverse_lazy('barbeiro-list')
    success_message = 'Barbeiro cadastrado com sucesso.'


class BarbeiroUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Barbeiro
    form_class = BarbeiroForm
    template_name = 'core/form.html'
    success_url = reverse_lazy('barbeiro-list')
    success_message = 'Barbeiro atualizado com sucesso.'


class BarbeiroDeleteView(LoginRequiredMixin, DeleteMessageMixin, DeleteView):
    model = Barbeiro
    template_name = 'core/confirm_delete.html'
    success_url = reverse_lazy('barbeiro-list')
    success_message = 'Barbeiro excluído com sucesso.'


class ServicoListView(ProtectedListView):
    model = Servico
    template_name = 'core/servico_list.html'
    context_object_name = 'servicos'


class ServicoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Servico
    form_class = ServicoForm
    template_name = 'core/form.html'
    success_url = reverse_lazy('servico-list')
    success_message = 'Serviço cadastrado com sucesso.'


class ServicoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Servico
    form_class = ServicoForm
    template_name = 'core/form.html'
    success_url = reverse_lazy('servico-list')
    success_message = 'Serviço atualizado com sucesso.'


class ServicoDeleteView(LoginRequiredMixin, DeleteMessageMixin, DeleteView):
    model = Servico
    template_name = 'core/confirm_delete.html'
    success_url = reverse_lazy('servico-list')
    success_message = 'Serviço excluído com sucesso.'


class AgendamentoListView(ProtectedListView):
    model = Agendamento
    template_name = 'core/agendamento_list.html'
    context_object_name = 'agendamentos'
    queryset = Agendamento.objects.select_related('cliente', 'barbeiro', 'servico').all()


class AgendamentoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Agendamento
    form_class = AgendamentoForm
    template_name = 'core/form.html'
    success_url = reverse_lazy('agendamento-list')
    success_message = 'Agendamento cadastrado com sucesso.'


class AgendamentoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Agendamento
    form_class = AgendamentoForm
    template_name = 'core/form.html'
    success_url = reverse_lazy('agendamento-list')
    success_message = 'Agendamento atualizado com sucesso.'


class AgendamentoDeleteView(LoginRequiredMixin, DeleteMessageMixin, DeleteView):
    model = Agendamento
    template_name = 'core/confirm_delete.html'
    success_url = reverse_lazy('agendamento-list')
    success_message = 'Agendamento excluído com sucesso.'
