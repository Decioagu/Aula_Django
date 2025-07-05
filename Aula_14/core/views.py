from django.views.generic import TemplateView

#14 classe IndexView
class IndexView(TemplateView):
    template_name = 'index.html'

