from django.views.generic.base import TemplateView
from django.forms.formsets import formset_factory
from .forms import ArticleForm


class formsetView(TemplateView):
    template_name = 'formsets/formsets.html'

    def get_context_data(self, **kwargs):
        context = super(formsetView, self).get_context_data(**kwargs)
        ArticleFormSet = formset_factory(ArticleForm, extra=2)
        context['formset'] = ArticleFormSet()
        return context