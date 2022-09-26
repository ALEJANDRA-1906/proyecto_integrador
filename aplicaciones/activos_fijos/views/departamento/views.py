from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView
from aplicaciones.activos_fijos.forms import  DepartamentoForm
from aplicaciones.activos_fijos.models import Departamento


class ListDepartamento(ListView):
    template_name = "departamento/list.html"
    model = Departamento
    context_object_name = 'Departamento'
    paginate_by = 3
    #queryset = Cliente.objects.filter(estado=True)

    def get_queryset(self):
        query = self.request.GET.get("query")
        print(query)
        if query:
            return self.model.objects.filter(nombre__icontains=query)
        else:
            return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_anterior'] = '/menu_ac'
        context['listar_url']= '/listdepartamento'
        context['crear_url'] = '/creardepartamento'
        context['titulo'] = 'LISTADO DE DEPARTAMENTOS'
        context['query'] = self.request.GET.get("query") or ""
        return context

class CrearDepartamento(CreateView):
    model = Departamento
    template_name = "departamento/form.html"
    success_url = reverse_lazy('activos_fijos:listdepartamento')
    form_class = DepartamentoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = '/creardepartamento/'
        context['titulo'] = 'CREAR DEPARTAMENTO'
        context['listar_url'] = '/listdepartamento'
        context['action'] = 'add'
        context['boton'] = 'Guardar'
        return context

class ActualizarDepartamento(UpdateView):
    model = Departamento
    template_name = "departamento/form.html"
    success_url = reverse_lazy('activos_fijos:listdepartamento')
    form_class = DepartamentoForm
    #queryset = Cliente.objects.get(pk=request.GET.get("id"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ACTUALIZAR DEPARTAMENTO'
        context['url_anterior'] = '/listdepartamento/'
        context['listar_url'] = '/listdepartamento/'
        context['boton'] = 'Actualizar'
        return context

class EliminarDepartamento(DeleteView):
    model = Departamento
    template_name = "departamento/delete.html"
    success_url = reverse_lazy('activos_fijos:listdepartamento')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ELMINAR CATEGORIA'
        context['listar_url'] = '/listdepartamento/'
        context['boton'] = 'Eliminar'
        return context
