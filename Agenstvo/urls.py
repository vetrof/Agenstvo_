from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),                # main.app
    path('zayavka/', include('zayavki.urls', namespace='zayavki')),  # zayavki.app
    path('search/', include('search.urls', namespace='search')),     # search.app
    path('api/', include('api.urls', namespace='api')),              # api
]
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
