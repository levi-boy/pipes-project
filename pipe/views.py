from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from . import models


class PipeListView(ListView):
    model = models.PipeModel
    context_object_name = 'pipes'
    template_name = 'pipe/pipe_list.html'


class PipeDetailView(DetailView):
    model = models.PipeModel
    context_object_name = 'pipe'
    template_name = 'pipe/pipe_detail.html'


def about(request):
    return render(request, 'views/about.html')
