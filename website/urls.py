from website.views import (IndexTemplateView, ComercioListView,
    ComercioCreateView, ComercioUpdateView, ComercioDeleteView,
    GastoListView, GastoCreateView, GastoUpdateView,
    GastoDeleteView, GastoComercioListView)

from django.urls import path

app_name = "website"

urlpatterns = [
    path('',IndexTemplateView.as_view(),name="index"),
    path('gastos/',GastoListView.as_view(),name="lista_gastos"),
    path('gastosPorComercio/<slug>/',GastoComercioListView.as_view(),name="lista_gastosPorComercio"),
    path('gasto/cadastrar',GastoCreateView.as_view(),name="cadastra_gasto"),
    path('gasto/<pk>',GastoUpdateView.as_view(),name="atualiza_gasto"),
    path('gasto/excluir/<pk>',GastoDeleteView.as_view(),name="deleta_gasto"),
    path('comercios/',ComercioListView.as_view(),name="lista_comercios"),
    path('comercio/cadastrar',ComercioCreateView.as_view(),name="cadastra_comercio"),
    path('comercio/<slug>',ComercioUpdateView.as_view(),name="atualiza_comercio"),
    path('comercio/excluir/<slug>',ComercioDeleteView.as_view(),name="deleta_comercio"),
]
