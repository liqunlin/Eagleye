from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template.context import RequestContext
from models import Student

#添加	
def beginAdd(request):
	return render_to_response('add.html')

#保存添加后的数据	
def add(request):
	id=request.POST['id']
	name=request.POST['name']
	age=request.POST['age']
	st=Student()
	if len(id)>0:
		print "id 不是null"
		st.id=id
	st.age=age
	st.name=name
	st.save()
	return HttpResponseRedirect('/index.html')

#查询所有信息	
def query(request):
	b=Student.objects.all()
	return render_to_response('curd.html',{'data':b})

#显示一条数据	
def showUid(request):
	id=request.GET['id']
	bb=Student.objects.get(id=id)
	return render_to_response('update.html',{'data':bb})

#删除数据	
def delByID(request):
	id=request.GET['id']
	bb=Student.objects.get(id=id)
	bb.delete()
	return HttpResponseRedirect('/index.html')

