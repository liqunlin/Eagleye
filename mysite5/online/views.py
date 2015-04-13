#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from models import User

#表单
class UserForm(forms.Form):
	username=forms.CharField(label='用户名',max_length=100)
	password=forms.CharField(label='密码',widget=forms.PasswordInput())
	
#注册
def regist(request):
	if request.method == 'POST':
		uf=UserForm(request.POST)
		if uf.is_valid():
			username=uf.cleaned_data['username']#获得表单用户密码
			password=uf.cleaned_data['password']
			User.objects.create(username=username,password=password)
			#print username,password
			#return HttpResponseRedirect('/online/login/')
			return HttpResponse('注册成功!!')
	else:
		uf=UserForm()
	return render_to_response('regist.html',{'uf':uf})
	#return render_to_response('regist.html',{'uf':uf},context_instance=RequestContext(request))

#登录
def login(request):
	if request.method == 'POST':
		uf=UserForm(request.POST)
		if uf.is_valid():
			username=uf.cleaned_data['username']
			password=uf.cleaned_data['password']
			user=User.objects.filter(username__exact=username,password__exact=password)#获取的表单数据与数据库进行比较
			if user:
				response=HttpResponseRedirect('/online/index/')#比较成功，跳转index 
				response.set_cookie('username',username,3600)
				return response
			else:
				return HttpResponseRedirect('/online/login/')
		else:
			uf=UserForm()
		return render_to_response('login.html',{'uf':uf})
		#return render_to_response('login.html',{'uf':uf},context_instance=RequestContext(request))

#登录成功
def index(request):
	username=request.COOKIES.get('username','')
	return render_to_response('index.html',{'username':username})

#退出
def logout(request):
	response=HttpResponse('退出!!')
	response.delete_cookie('username')#清理cookie里保存username
	return response


