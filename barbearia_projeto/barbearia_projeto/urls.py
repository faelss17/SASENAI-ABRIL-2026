from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from core.api_views import AgendamentoViewSet, BarbeiroViewSet, ClienteViewSet, ServicoViewSet
from core.views import DashboardView

router = DefaultRouter()
router.register('clientes', ClienteViewSet, basename='api-clientes')
router.register('barbeiros', BarbeiroViewSet, basename='api-barbeiros')
router.register('servicos', ServicoViewSet, basename='api-servicos')
router.register('agendamentos', AgendamentoViewSet, basename='api-agendamentos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', DashboardView.as_view(), name='dashboard'),
    path('', include('core.urls')),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
