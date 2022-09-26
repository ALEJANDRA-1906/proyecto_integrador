from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView
from aplicaciones.activos_fijos.forms import ActivoForm
from aplicaciones.activos_fijos.models import Activo

class ActivoListView(ListView):
    template_name = "activo/list.html"
    model = Activo
    context_object_name = 'activos'
    paginate_by = 3
    #queryset = Cliente.objects.filter(estado=True)

    def get_queryset(self):
        query = self.request.GET.get("query")
        print(query)
        if query:
            return self.model.objects.filter(nombres__icontains=query)
        else:
            return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_anterior'] = '/activos/menu_ac'
        context['listar_url'] = '/activo'
        context['crear_url'] = '/activos/crearactivo/'
        context['titulo'] = 'LISTADO DE ACTIVOS'

        context['query'] = self.request.GET.get("query") or ""
        return context

class CrearActivo(CreateView):
    model = Activo
    template_name = "activo/form.html"
    success_url = reverse_lazy('activos_fijos:activo')
    form_class = ActivoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = '/activos/crearactivo/'
        context['titulo'] = 'CREAR ACTIVO'
        context['url_anterior'] = '/activos/activo/'
        context['listar_url'] = '/activos/activo/'
        context['action'] = 'add'
        return context
