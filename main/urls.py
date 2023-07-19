from django.urls import path

from .views import ObjectsMain, detailobjectview, ManagerDetailView

app_name = 'main'

# ''/
urlpatterns = [
    path('', ObjectsMain.as_view(), name='home'),
    path('detail/<int:pk>/', detailobjectview, name='object_info'),
    path('manager/<int:pk>/', ManagerDetailView.as_view(), name='manager_info'),


]
