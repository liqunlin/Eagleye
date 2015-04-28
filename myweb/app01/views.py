from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template.context import RequestContext
from models import Student,ItDeviceManage

#单独添加新数据	
def beginAdd(request):
	return render_to_response('add.html')
#添加新数据(点击按键添加)
def add(request):
	all_fields=['id','username','department','device_id','device_variety','device_sub_variety','device_type','serial_number','usage_state','remark']
	for t in all_fields:
		exec("%s=request.POST['%s']" %(t,t))
		#范例：username=request.POST['username']
	idm=ItDeviceManage()
	if len(id)>0:
		print "id 不是null"
		idm.id=id
	for i in all_fields:
		if i is 'id':
			pass
		else:
			exec('idm.%s=%s' %(i,i))
			#范例：idm.username=username
	idm.save()
	return HttpResponseRedirect('/index.html')
#查询所有数据	
def query(request):
	b=ItDeviceManage.objects.all()
	return render_to_response('main.html',{'data':b})
#修改数据	
def updateByID(request):
	id=request.GET['id']
	bb=ItDeviceManage.objects.get(id=id)
	return render_to_response('update.html',{'data':bb})
#删除数据	
def delByID(request):
	id=request.GET['id']
	bb=ItDeviceManage.objects.get(id=id)
	bb.delete()
	return HttpResponseRedirect('/index.html')
	
