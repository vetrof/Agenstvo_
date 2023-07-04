from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from main.models import Realty, Category, Manager
from zayavki.forms import ZayavkaForm


# class AllObjects(ListView):
#     model = Realty
#     template_name = 'main.html'
#     context_object_name = 'objects'


class ObjectsMain(ListView):
    model = Realty
    template_name = 'main.html'
    context_object_name = 'realty'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.all()
        context['category'] = category
        return context

    def get_queryset(self):
        query = self.request.GET.get('zapros')
        min = self.request.GET.get('min')
        max = self.request.GET.get('max')

        if query:
            queryset = Realty.objects.filter(Q(info__icontains=query) | Q(title__icontains=query))
        else:
            queryset = Realty.objects.all()

        if min:
            queryset = queryset.filter(price__gt=min)

        if max:
            queryset = queryset.filter(price__lte=max)
        return queryset


def detailobjectview(request, pk):
    info = Realty.objects.get(pk=pk)

    if request.method == 'POST':
        form = ZayavkaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = ZayavkaForm()
    return render(request, 'detail.html', {'info': info, 'form': form})


class ManagerDetailView(DetailView):
    template_name = 'manager_info.html'
    model = Manager
    context_object_name = 'manager_info'
