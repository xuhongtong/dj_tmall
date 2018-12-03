from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from dj_tmall import settings
from apps.main.models import ShopCar, Shop
from django.conf import settings

# def axjx_login_required(func):
#     def inner(request, *args, **kwargs):
#         if request.user.is_authenticated():
#             return func(request, *args, **kwargs)
#         else:
#             return redirect(settings.LOGIN_URL.join('?next=').join(request.path))
#     return inner
#
# @axjx_login_required


#接收加入购物车发送的请求数据（ajax请求会通过get或post请求发送data数据

def add_cart(request):
    result={'status':200,'msg':'ok'}
    try:
        number = request.POST.get('number')
        shop_id = request.POST.get('shop_id')

        #商品数量初始值为0
        update_number = 0
        # 商品存在就更新数量（这里初始值为1）
        if ShopCar.objects.filter(shop_id=shop_id,user_id=request.user.id,status=1):
            shop = ShopCar.objects.update(number=F('number') + number)
        # 如果商品不存在将商品数量设置为1，并保存
        else:
            update_number = 1
            shop = ShopCar(number=number, shop_id=shop_id, user_id=request.user.id)
            shop.save()
        shop_num=ShopCar.objects.values_list('shop_id',flat=True).count()
        # result.update(data=number)
        result.update(data=shop_num)
        return JsonResponse(result)
    except Exception as e:
        result={'status':400,'msg':'添加失败'}



#购物车页面
def shopcat(request):

    #获取登陆用户购物车商品添加记录
    shop_carts = ShopCar.objects.filter(user_id=request.user.id,status=1)
    for shop_cart in shop_carts:
        #获取商品图片
        shop_cart.img=shop_cart.shop.shopimage_set.all().first()

    #前端需要渲染的数据
    context={
        'shop_carts':shop_carts,
    }
    return render(request,'shopcat.html',context)



def delcat(request):
    result = {'status': 200, 'msg': 'ok'}
    try:
        car_id=request.GET.get('car_id')
        ShopCar.objects.filter(car_id=car_id).update(status=-1)
        return JsonResponse(result)
    except:
        result = {'status': 400, 'msg': '删除失败'}