from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView
from aplicaciones.activos_fijos.forms import CategoriaForm
from aplicaciones.activos_fijos.models import Categoria

class ListCategoria(ListView):
    template_name = "categoria/list.html"
    model = Categoria
    context_object_name = 'Categoria'
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
        context['listar_url']= '/listcategoria'
        context['crear_url'] = '/crearcategoria'
        context['titulo'] = 'LISTADO DE CATEGORIAS'
        context['query'] = self.request.GET.get("query") or ""
        return context

class CrearCategoria(CreateView):
    model = Categoria
    template_name = "categoria/form.html"
    success_url = reverse_lazy('activos_fijos:listcategoria')
    form_class = CategoriaForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = '/crearcategoria/'
        context['titulo'] = 'CREAR CATEGORIA'
        context['listar_url'] = '/listcategoria'
        context['action'] = 'add'
        context['boton'] = 'Guardar'
        return context

class ActualizarCategoria(UpdateView):
    model = Categoria
    template_name = "categoria/form.html"
    success_url = reverse_lazy('activos_fijos:listcategoria')
    form_class = CategoriaForm
    #queryset = Cliente.objects.get(pk=request.GET.get("id"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ACTUALIZAR CATEGORIA'
        context['url_anterior'] = '/listcategoria/'
        context['listar_url'] = '/listcategoria/'
        context['boton'] = 'Actualizar'
        return context


class EliminarCategoria(DeleteView):
    model = Categoria
    template_name = "categoria/delete.html"
    success_url = reverse_lazy('activos_fijos:listcategoria')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ELMINAR CATEGORIA'
        context['listar_url'] = '/listcategoria/'
        context['boton'] = 'Eliminar'
        return context
