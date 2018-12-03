from django.conf.urls import url

from apps.cart import views

urlpatterns = [
    url('add_cart',views.add_cart,name='add_cart'),
    url('addcart',views.shopcat,name='cart'),
    url('delcart',views.delcat,name='delcart'),
]