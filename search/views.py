from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView

from main.models import Realty, Category


class SearchResult(ListView):
    template_name = 'search_result.html'
    model = Realty
    context_object_name = 'Realty'

    def get_queryset(self):
        query = self.request.GET.get('zapros')
        min = self.request.GET.get('min')
        max = self.request.GET.get('max')
        category = self.request.GET.get('category')

        if query:
            queryset = Realty.objects.filter(Q(info__iregex=query) | Q(title__iregex=query))

        else:
            queryset = Realty.objects.all()

        if min:
            queryset = queryset.filter(price__gt=min)

        if max:
            queryset = queryset.filter(price__lte=max)

        if category:
            queryset = queryset.filter(cat=category)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.all()
        context['category'] = category
        return context
