from django.urls import path, include
from rest_framework import routers

from api.views import RealtyViewSet, ZayavkaCreateView, SearchApi, CategoriesApi

router = routers.DefaultRouter()
router.register('realty', RealtyViewSet)
router.register('zayavka', ZayavkaCreateView)
router.register('search', SearchApi)
router.register('categories', CategoriesApi)

app_name = 'api'
# /api/
urlpatterns = [
    path('', include(router.urls)),
]
