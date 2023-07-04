from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from mail_sender.views import test_mail
from main.views import detailobjectview, ManagerDetailView, ObjectsMain
from search.views import SearchResult
from zayavki.views import ZayavkaViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ObjectsMain.as_view(), name='home'),

    # Realty
    # path('<int:category>/', all_objects, name='category'),
    path('detail/<int:pk>/', detailobjectview, name='object_info'),

    # manager
    path('manager/<int:pk>/', ManagerDetailView.as_view(), name='manager_info'),

    path('zayavka/', ZayavkaViews.as_view(), name='zayavka'),

    path('search/', SearchResult.as_view(), name='search'),


    path('test_mail/', test_mail)
]


if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



