from django.conf.urls import url

from apps.search import views

urlpatterns = [
    url('^$',views.search,name='search'),
]