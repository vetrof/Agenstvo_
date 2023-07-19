from urllib.parse import urlencode

from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic import TemplateView
from rest_framework import generics, viewsets, status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import RealtySerializer, ZayavkaSerializer, AllCategories
from main.models import Realty, Category
from zayavki.models import Zayavka


class RealtyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Realty.objects.all()
    serializer_class = RealtySerializer


class ZayavkaCreateView(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Zayavka.objects.all()
    serializer_class = ZayavkaSerializer
    http_method_names = ['post']


class SearchApi(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Realty.objects.all()
    serializer_class = RealtySerializer
    http_method_names = ['get']
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

        # paginator = Paginator(queryset, 9)
        # page_number = self.request.GET.get('page', 1)
        # queryset = paginator.page(page_number)

        return queryset


class CategoriesApi(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = AllCategories
    http_method_names = ['get']
