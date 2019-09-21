from django.shortcuts import render
from product.models import Product
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
#产品管理
def product_manage(request):
	username = request.session.get('user','')
	product_list = Product.objects.all()
	product_count = product_list.count() #统计产品数
	paginator = Paginator(product_list,8)#设置每页记录为8条
	page = request.GET.get('page',1)#获取当前页码数，默认为1
	currentPage = int(page)#把获取的当前页码数转换成整形
	try:
		product_list = paginator.page(page)#获取当前页码的记录列表
	except PageNotAnInteger:
		product_list = paginator.page(1)#输入的页数不是整数，显示第一页
	except EmptyPage:
		product_list = paginator.page(paginator.num_pages)#输入不存在的页数，显示最后一页
	return render(request, "product_manage.html", {"user":username,"products":product_list,"productcounts": product_count})
@login_required 
def productsearch(request): 
	username = request.session.get('user', '') # 读取浏览器登录Session 
	search_productname = request.GET.get("productname", "") 
	product_list = Product.objects.filter(productname__icontains=search_productname) 
	return render(request,'product_manage.html', {"user": username,"products":product_list})
