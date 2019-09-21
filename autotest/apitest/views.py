from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate,login
from apitest.models import Apitest,Apistep,Apis
import pymysql
# Create your views here.
def test(request):
	return HttpResponse("hello test")
def login(request):
	if request.POST:
		username = password = ''
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = auth.authenticate(username=username, password=password)
		if user is not None and user.is_active:
			auth.login(request, user)
			request.session['user'] = username
			response = HttpResponseRedirect('/home/')
			return response
		else:
			return render(request,'login.html',{'error': 'username or password error'})
	#else:
	#	content = {}
	#	return render(request,'login.html',context)
	return render(request,'login.html')
def home(request): 
	return render(request,"home.html")
def logout(request):
	auth.logout(request)
	return render(request, 'login.html')
	
#接口管理
@login_required
def apitest_manage(request):
	apitest_list = Apitest.objects.all()#读取所有流程接口数据
	username = request.session.get('user','')#读取浏览器登录Session
	return render(request,"apitest_manage.html",{"user":username,"apitests":apitest_list})#自定义流程接口数据的变量并返回到前端
#接口步骤管理
@login_required
def apistep_manage(request):
	username = request.session.get('user','')
	apistep_list = Apistep.objects.all()
	return render(request,"apistep_manage.html",{"user":username,"apisteps":apistep_list})
#单一接口管理
@login_required
def apis_manage(request):
	username = request.session.get('user','')
	apis_list = Apis.objects.all()
	return render(request,"apis_manage.html",{"user":username,"apis":apis_list})
#测试报告
@login_required
def test_report(request):
	username = request.session.get('user', '')
	apis_list = Apis.objects.all()
	apis_count = Apis.objects.all().count()
	db = pymysql.connect(user='root', db='autotest', password='123456', host='127.0.0.1')
	cursor = db.cursor()
	sql1 = 'SELECT count(id) FROM apitest_apis WHERE apitest_apis.apistatus=1'
	aa = cursor.execute(sql1)
	apis_pass_count = [row[0] for row in cursor.fetchmany(aa)][0]
	sql2 = 'SELECT count(id) FROM apitest_apis WHERE apitest_apis.apistatus=0'
	bb = cursor.execute(sql2)
	apis_fail_count = [row[0] for row in cursor.fetchmany(bb)][0]
	db.close()
	return render(request, "report.html", {"user": username, "apis": apis_list, "apiscounts": apis_count, "apis_pass_counts": apis_pass_count, "apis_fail_counts": apis_fail_count})
def left(request):
	return render(request,"left.html")
def report(request):
	return render(request,"report.html")
#搜索功能
@login_required
def apisearch(request):
	username = request.session.get('user', '')
	search_apitestname = request.GET.get("apitestname", "")
	apitest_list = Apitest.objects.filter(apitestname__icontains=search_apitestname)
	return render(request,'apitest_manage.html',{"user": username, "apitests": apitest_list})
@login_required
def apistepsearch(request):
	username = request.session.get('user', '')
	search_apistepname = request.GET.get("apistepname", "")
	apistep_list = Apistep.objects.filter(apiname__icontains=search_apistepname)
	return render(request,'apistep_manage.html',{"user": username, "apisteps": apistep_list})
@login_required
def apissearch(request):
	username = request.session.get('user', '')
	search_apisname = request.GET.get("apiname", "")
	apis_list = Apis.objects.filter(apiname__icontains=search_apisname)
	return render(request,'apis_manage.html',{"user": username, "apis": apis_list})

	