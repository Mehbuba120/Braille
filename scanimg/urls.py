from django.urls.conf import path

from . import views

app_name = 'scanimg'

urlpatterns = [
    path('', views.scan, name='photo'),
]