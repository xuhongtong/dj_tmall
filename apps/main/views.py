from django.shortcuts import render

# Create your views here.
# from main.model import Navigation
# from main.models import Navigation
#
#
from apps.main.models import Navigation, Category, SubMenu, Shop, ShopImage


def index(request):
    # 获取所有导航表记录
    nav_list = Navigation.objects.all()
    # 查询分类表所有记录并以id倒序排序
    cate_list = Category.objects.all().order_by('-cate_id')
    # 查询二级分类表所有记录并以id倒序排序
    sub_list = SubMenu.objects.all().order_by('-sub_menu_id')

    # 通过分类表反向查询子表（二级分类表）记录（一对多查询），并将其查询结果（列表）赋值给创建的动态变量（主表），每个动态变量对应多个二级菜单
    for cate in cate_list:
        li = cate.submenu_set.all()
        cate.sub_list = li

    # 通过分类表反向查询子表（shop表记录）记录（一对多查询），并将其查询结果（列表）赋值给创建的动态变量（主表），每个动态变量对应多条shop记录
    for cate in cate_list:
        li = cate.shop_set.all()
        cate.shop_list = li

    # 将分类表中动态创建的变量进行变量（获得单条二级记录），然后反向查询子表（三级分类表）记录（一对多查询），并将其查询结果（列表）赋值给创建的动态变量（二级分类表-主表），每个动态变量对应多个三级菜单
    for sub in sub_list:
        li = sub.submenu2_set.all()
        sub.sub2_list = li

    # 获取前5条shop记录
    shops = Shop.objects.all()[0:5]

    context = {
        'nav_list': nav_list,
        'cate_list': cate_list,
        'sub_list': sub_list,
        'shops': shops,
    }
    return render(request, 'index.html', context)



