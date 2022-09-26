from django.urls import path

from .views.activo.views import ActivoListView, CrearActivo
from .views.categoria.views import ListCategoria, CrearCategoria, ActualizarCategoria, EliminarCategoria
from .views.departamento.views import ListDepartamento, CrearDepartamento, ActualizarDepartamento, EliminarDepartamento
from .views.menu_act.views import MenuTemplateView


app_name = "activos_fijos"
urlpatterns = [

    # activo
    path('activo', ActivoListView.as_view(), name='activo'),
    path('crearactivo/', CrearActivo.as_view(), name='crearactivo'),

    # empleado
    path('menu_ac', MenuTemplateView.as_view(), name="menu_ac"),

    # categoria
    path('listcategoria/', ListCategoria.as_view(), name='listcategoria'),
    path('crearcategoria/', CrearCategoria.as_view(), name='crearcategoria'),
    path('actualizarcategoria/<int:pk>', ActualizarCategoria.as_view(), name='actualizarcategoria'),
    path('eliminarcategoria/<int:pk>', EliminarCategoria.as_view(), name='eliminarcategoria'),

    # departamento
    path('listdepartamento/', ListDepartamento.as_view(), name='listdepartamento'),
    path('creardepartamento/', CrearDepartamento.as_view(), name='creardepartamento'),
    path('actualizardepartamento/<int:pk>', ActualizarDepartamento.as_view(), name='actualizardepartamento'),
    path('eliminardepartamento/<int:pk>', EliminarDepartamento.as_view(), name='eliminardepartamento'),



]