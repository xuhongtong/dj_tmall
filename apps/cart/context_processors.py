
from apps.main.models import ShopCar


def count(request):
    shop_num = ShopCar.objects.values('shop_id').filter(user_id=request.user.id,status=1).count()
    return {'shop_num':shop_num}