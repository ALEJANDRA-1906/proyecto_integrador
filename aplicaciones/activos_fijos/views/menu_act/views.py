from django.views.generic.base import TemplateView

class MenuTemplateView(TemplateView):
    template_name = 'menu_ac.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Activos"
        context['url_anterior1'] = "/"
        return context
