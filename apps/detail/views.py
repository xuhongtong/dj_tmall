from django.shortcuts import render

# Create your views here.
from apps.main.models import Shop


def detail(request):
    # 获取url中的shop_id参数
    shop_id = request.GET.get('shop_id')
    # 获取单条商品详情记录
    shop = Shop.objects.get(shop_id=shop_id)
    # 获取商品详情键
    property_list = shop.cate.property_set.all()
    # 获取商品图片介绍
    imgs = shop.shopimage_set.all()
    # 查询商品详情值
    value_list = shop.propertyvalue_set.all()

    #获取评论
    reviews=shop.review_set.all()

    context = {
        'shop': shop,
        'imgs': imgs,
        'property_list': property_list,
        'value_list': value_list,
        'reviews':reviews,
    }
    return render(request, 'detail.html', context)