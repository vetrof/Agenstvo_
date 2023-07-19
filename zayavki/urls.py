from django.urls import path

from zayavki.views import ZayavkaViews

app_name = 'zayavki'

# /zayavka/
urlpatterns = [
    path('', ZayavkaViews.as_view(), name='zayavka'),
]