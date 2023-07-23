from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from main.models import Realty, Category, Manager
from zayavki.forms import ZayavkaForm


# list objects on index page
class ObjectsMain(ListView):
    model = Realty
    template_name = 'main.html'
    context_object_name = 'realty'

    def get_queryset(self):
        queryset = super().get_queryset()
        rnd_obj = Realty.objects.order_by('?')[:3]
        return rnd_obj


def detailobjectview(request, pk):
    info = Realty.objects.get(pk=pk)

    if request.method == 'POST':
        form = ZayavkaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:home')
    else:
        form = ZayavkaForm()
    return render(request, 'detail.html', {'info': info, 'form': form})




class ManagerDetailView(DetailView):
    template_name = 'manager_info.html'
    model = Manager
    context_object_name = 'manager_info'
