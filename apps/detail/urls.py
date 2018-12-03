from django.conf.urls import url

from apps.detail import views

urlpatterns = [
    url('^$',views.detail,name='detail'),
]