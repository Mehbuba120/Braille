"""braille URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls.conf import include, path
from django.conf.urls.static import settings, static

from .views import (AboutView, HelpView, IndexView,
                    SignUpView, UserDetailView)
                     #ScanView,

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    #path('contact/', ContactView.as_view(), name='contact'),
    path('help/', HelpView.as_view(), name='help'),
   # path('scan/', ScanView.as_view(), name='scan'),

    path('profile/<slug:pk>/', UserDetailView.as_view(), name='profile'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('contact/', include('contact.urls')),
    path('scanimg', include('scanimg.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
 # accounts/login/
    # accounts/logout/
    # accounts/password_change/
    # accounts/password_reset/
    # accounts/login/