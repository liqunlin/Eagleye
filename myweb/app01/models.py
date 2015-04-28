from django.db import models
	
class ItDeviceManage(models.Model):
	username=models.CharField(max_length=50)
	department=models.CharField(max_length=100)
	device_id=models.CharField(max_length=100)
	device_variety=models.CharField(max_length=50)
	device_sub_variety=models.CharField(max_length=50)
	device_type=models.CharField(max_length=50)
	serial_number=models.CharField(max_length=50)
	usage_state=models.CharField(max_length=50)
	remark=models.CharField(max_length=100)
	
#class ServerManage(models.Model):
#	server_id=models.CharField(max_length=100)
#	appname=models.CharField(max_length=100)
#	machine_type=models.CharField(max_length=50,null=True)
#	runstate=models.CharField(max_length=20)
#	private_ip=models.IntegerField()
#	cpu=models.CharField(max_length=20)
#	mem=models.CharField(max_length=20)
#	disk=models.CharField(max_length=20)
#	system=models.CharField(max_length=50)
	
