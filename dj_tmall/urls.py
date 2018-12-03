"""dj_tmall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url,include

from apps.main import views
import xadmin

urlpatterns = [
    url('xadmin/',xadmin.site.urls),
    url('admin/', admin.site.urls),
    url('^$',views.index),
    # url('main/',include('main.urls')),
    url('search',include('search.urls')),
    url('cart/',include('cart.urls')),
    url('detail',include('detail.urls')),
    url('account/',include('account.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)