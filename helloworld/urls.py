from django.urls import include, path
from django.contrib import admin
from django.contrib.auth.views import login, logout

from core import views

urlpatterns = [
    # URL padrão
    path('', views.index, name='index'),
    path('entrar/', login, {'template_name':'accounts/login.html'}, name='login'),
    path('sair/', logout, {'next_page':'index'}, name='logout'),
    path('conta/', include('accounts.urls')),
    path('website/', include('website.urls')),
    # Interface administrativa
    path('admin/', admin.site.urls),
]
