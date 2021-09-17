from django.views import generic
from . import models

class IndexView(generic.TemplateView):
    template_name = 'doeagora/index.html'
