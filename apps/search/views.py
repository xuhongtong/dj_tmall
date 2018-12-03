from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from apps.main.models import Shop, ShopImage


def search(request):
    keyword=request.GET.get('keyword')
    results=Shop.objects.filter(Q(name__contains=keyword)|Q(sub_title__contains=keyword)).values('shop_id','promote_price','name','sub_title')
    for result in results:
        # img=result.shopimage_set.all().first()
        img=ShopImage.objects.filter(shop_id=result.get('shop_id')).first()
        result.update(img=img.shop_img_id)
    context={
        'results':results,
    }
    return render(request,'search.html',context)