from django import forms

from .models import Agendamento, Barbeiro, Cliente, Servico


class BaseBootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            css_class = 'form-control'
            if isinstance(field.widget, forms.CheckboxInput):
                css_class = 'form-check-input'
            field.widget.attrs.setdefault('class', css_class)


class ClienteForm(BaseBootstrapModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'telefone', 'email']


class BarbeiroForm(BaseBootstrapModelForm):
    class Meta:
        model = Barbeiro
        fields = ['nome', 'especialidade', 'telefone', 'ativo']


class ServicoForm(BaseBootstrapModelForm):
    class Meta:
        model = Servico
        fields = ['nome', 'descricao', 'preco', 'duracao_estimada']


class AgendamentoForm(BaseBootstrapModelForm):
    data = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    horario = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}))

    class Meta:
        model = Agendamento
        fields = ['cliente', 'barbeiro', 'servico', 'data', 'horario', 'status', 'observacoes']
