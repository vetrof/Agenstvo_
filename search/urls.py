from django.urls import path

from search.views import SearchResult

app_name = 'search'

urlpatterns = [
    path('', SearchResult.as_view(), name='search'),
]
