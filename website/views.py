from django.urls import reverse_lazy
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from .models import Comercio, Gasto
from website.forms import InsereComercioForm, InsereGastoForm
from django.contrib.auth.mixins import LoginRequiredMixin


# PÁGINA PRINCIPAL
# ----------------------------------------------

class IndexTemplateView(LoginRequiredMixin, generic.TemplateView):
    template_name = "index.html"

# LISTA DE GASTOS
# ----------------------------------------------

class GastoListView(LoginRequiredMixin, generic.ListView):
    template_name = "website/lista_gastos.html"
    model = Gasto
    context_object_name = "gastos"
    paginate_by = 5

# LISTA DE GASTOS DE UM COMÉRCIO ESPECÍFICO
# ----------------------------------------------

class GastoComercioListView(LoginRequiredMixin, generic.ListView):

    template_name = "website/lista_gastosPorComercio.html"
    context_object_name = "gastos"
    paginate_by = 5

    def get_queryset(self):
        return Gasto.objetos.filter(comercio__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(GastoComercioListView, self).get_context_data(**kwargs)
        context['current_comercio'] = get_object_or_404(Comercio, slug=self.kwargs['slug'])
        return context

gastoComercio = GastoComercioListView.as_view()

# CADASTRAMENTO DE GASTOS
# ----------------------------------------------

class GastoCreateView(generic.CreateView):
    template_name = "website/cria_gasto.html"
    model = Gasto
    form_class = InsereGastoForm
    success_url = reverse_lazy("website:lista_gastos")

# ATUALIZAÇÃO DE GASTOS
# ----------------------------------------------

class GastoUpdateView(generic.UpdateView):
    template_name = "website/atualiza_gasto.html"
    model = Gasto
    fields = '__all__'
    context_object_name = 'gasto'
    success_url = reverse_lazy("website:lista_gastos")

    def get_object(self, queryset=None):
      gasto = None

      # Se você utilizar o debug, verá que os
      # campos {pk} e {slug} estão presente em self.kwargs
      id = self.kwargs.get(self.pk_url_kwarg)
      slug = self.kwargs.get(self.slug_url_kwarg)

      if id is not None:
        # Busca o gasto apartir do id
        gasto = Gasto.objetos.filter(id=id).first()

      elif slug is not None:
        # Pega o campo slug do Model
        campo_slug = self.get_slug_field()

        # Busca o gasto apartir do slug
        gasto = Gasto.objetos.filter(**{campo_slug: slug}).first()

      # Retorna o objeto encontrado
      return gasto

# EXCLUSÃO DE GASTOS
# ----------------------------------------------

class GastoDeleteView(generic.DeleteView):
    template_name = "website/exclui_gasto.html"
    model = Gasto
    fields = '__all__'
    context_object_name = 'gasto'
    success_url = reverse_lazy("website:lista_gastos")

# LISTA DE COMÉRCIOS
# ----------------------------------------------

class ComercioListView(LoginRequiredMixin, generic.ListView):
    template_name = "website/lista_comercios.html"
    model = Comercio
    context_object_name = "comercios"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ComercioListView, self).get_context_data(**kwargs)
        list_exam = Comercio.objetos.all()
        paginator = Paginator(list_exam, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            file_exams = paginator.page(page)
        except PageNotAnInteger:
            file_exams = paginator.page(1)
        except EmptyPage:
            file_exams = paginator.page(paginator.num_pages)

        context['list_exams'] = file_exams
        return context

# CADASTRAMENTO DE COMÉRCIOS
# ----------------------------------------------

class ComercioCreateView(generic.CreateView):
    template_name = "website/cria_comercio.html"
    model = Comercio
    form_class = InsereComercioForm
    success_url = reverse_lazy("website:lista_comercios")

# ATUALIZAÇÃO DE COMÉRCIOS
# ----------------------------------------------

class ComercioUpdateView(generic.UpdateView):
    template_name = "website/atualiza_comercio.html"
    model = Comercio
    fields = '__all__'
    context_object_name = 'comercio'
    success_url = reverse_lazy("website:lista_comercios")

    def get_object(self, queryset=None):
      comercio = None

      # Se você utilizar o debug, verá que os
      # campos {pk} e {slug} estão presente em self.kwargs
      id = self.kwargs.get(self.pk_url_kwarg)
      slug = self.kwargs.get(self.slug_url_kwarg)

      if id is not None:
        # Busca o comercio apartir do id
        comercio = Comercio.objects.filter(id=id).first()

      elif slug is not None:
        # Pega o campo slug do Model
        campo_slug = self.get_slug_field()

        # Busca o comercio apartir do slug
        comercio = Comercio.objetos.filter(**{campo_slug: slug}).first()

      # Retorna o objeto encontrado
      return comercio

# EXCLUSÃO DE COMÉRCIOS
# ----------------------------------------------

class ComercioDeleteView(generic.DeleteView):
    template_name = "website/exclui_comercio.html"
    model = Comercio
    fields = '__all__'
    context_object_name = 'comercio'
    success_url = reverse_lazy("website:lista_comercios")

    def get_object(self, queryset=None):
      comercio = None

      # Se você utilizar o debug, verá que os
      # campos {pk} e {slug} estão presente em self.kwargs
      id = self.kwargs.get(self.pk_url_kwarg)
      slug = self.kwargs.get(self.slug_url_kwarg)

      if id is not None:
        # Busca o comercio apartir do id
        comercio = Comercio.objects.filter(id=id).first()

      elif slug is not None:
        # Pega o campo slug do Model
        campo_slug = self.get_slug_field()

        # Busca o comercio apartir do slug
        comercio = Comercio.objetos.filter(**{campo_slug: slug}).first()

      # Retorna o objeto encontrado
      return comercio
