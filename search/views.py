from urllib.parse import urlencode

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView

from main.models import Realty, Category

from django.contrib.auth.decorators import login_required


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
            search_terms = query.split()
            q_objects = Q()
            for term in search_terms:
                q_objects &= (Q(info__iregex=term) | Q(title__iregex=term))
            queryset = Realty.objects.filter(q_objects)

        else:
            queryset = Realty.objects.all()
        if min:
            queryset = queryset.filter(price__gt=min)
        if max:
            queryset = queryset.filter(price__lte=max)
        if category:
            queryset = queryset.filter(cat=category)

        paginator = Paginator(queryset, 9)
        page_number = self.request.GET.get('page', 1)
        queryset = paginator.page(page_number)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.all()

        all_get_query = self.request.GET.copy()
        all_get_query.pop('page', None)  # Удаляем параметр 'page'
        query_params = {}
        for k, v in all_get_query.items():  # Удаляем пустые значения
            if v:
                query_params[k] = v
        clean_query_string = urlencode(query_params)

        context['category'] = category
        context['clean_query_string'] = clean_query_string
        return context

