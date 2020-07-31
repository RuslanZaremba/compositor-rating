from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import HttpResponse

from .models import PlayList


class PlayListView(TemplateView):
    template_name = 'index.html'

    def prosmotr(self):
        return HttpResponse(f'RuslanZaremba')

    def get_context_data(self, **kwargs):
        context = super(PlayListView, self).get_context_data(**kwargs)
        context['Playlist'] = PlayList.objects.all()
        return context


class GetView(View):
    template_name = 'index2.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': 1})
