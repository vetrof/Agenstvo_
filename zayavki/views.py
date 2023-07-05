from django.shortcuts import render
from django.views.generic import CreateView

from zayavki.models import Zayavka


class ZayavkaViews(CreateView):
    template_name = 'zayavka.html'
    model = Zayavka
    fields = ('name', 'email', 'question')
    success_url = '/'
