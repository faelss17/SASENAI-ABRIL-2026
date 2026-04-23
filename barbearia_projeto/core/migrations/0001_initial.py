from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Barbeiro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('especialidade', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=20)),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={'verbose_name': 'Barbeiro', 'verbose_name_plural': 'Barbeiros', 'ordering': ['nome']},
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
            ],
            options={'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes', 'ordering': ['nome']},
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('descricao', models.TextField(blank=True)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8)),
                ('duracao_estimada', models.PositiveIntegerField(help_text='Duração em minutos')),
            ],
            options={'verbose_name': 'Serviço', 'verbose_name_plural': 'Serviços', 'ordering': ['nome']},
        ),
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('horario', models.TimeField()),
                ('observacoes', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('agendado', 'Agendado'), ('concluido', 'Concluído'), ('cancelado', 'Cancelado')], default='agendado', max_length=15)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('barbeiro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='agendamentos', to='core.barbeiro')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agendamentos', to='core.cliente')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='agendamentos', to='core.servico')),
            ],
            options={'verbose_name': 'Agendamento', 'verbose_name_plural': 'Agendamentos', 'ordering': ['data', 'horario']},
        ),
        migrations.AddConstraint(
            model_name='agendamento',
            constraint=models.UniqueConstraint(fields=('barbeiro', 'data', 'horario'), name='unique_horario_por_barbeiro'),
        ),
    ]
