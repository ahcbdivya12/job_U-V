from django.db import models

# Create your models here.
class registration(models.Model):
	name=models.CharField(max_length=40)
	email=models.CharField(max_length=40)
	password=models.CharField(max_length=40)
	cpassword=models.CharField(max_length=40)
	address=models.CharField(max_length=40)
	mobile=models.BigIntegerField()
	gender=models.CharField(max_length=40)
	state=models.CharField(max_length=40)


class contact(models.Model):
	c_name=models.CharField(max_length=40)
	email=models.CharField(max_length=40)
	mobile=models.BigIntegerField()
	messages=models.CharField(max_length=400)
	

class c_job(models.Model):
	f_name=models.CharField(max_length=40)
	l_name=models.CharField(max_length=40)
	address=models.CharField(max_length=40)
	city=models.CharField(max_length=20)
	zip_p=models.BigIntegerField()
	email=models.CharField(max_length=40)
	phone=models.IntegerField()
	gst_no=models.CharField(max_length=40)
	cln=models.BigIntegerField()
	job=models.CharField(max_length=40)
	language=models.CharField(max_length=40)
	salary=models.IntegerField()
	subject=models.CharField(max_length=90)
	iso_c=models.BinaryField()
	gmp_c=models.BinaryField()
	logo=models.BinaryField()

class sp_registration(models.Model):
	name=models.CharField(max_length=40)
	email=models.CharField(max_length=40)
	pass1=models.CharField(max_length=40)
	pass2=models.CharField(max_length=40)
	address=models.CharField(max_length=40)
	mobile=models.BigIntegerField()
	gender=models.CharField(max_length=40)
	state=models.CharField(max_length=40)

class sp_news(models.Model):
	subject=models.CharField(max_length=40)
	date_time=models.DateTimeField()
	title=models.CharField(max_length=40)
	sp_new=models.CharField(max_length=5000)


class quiz(models.Model):
	question=models.CharField(max_length=60)
	opt1=models.CharField(max_length=40)
	opt2=models.CharField(max_length=40)
	opt3=models.CharField(max_length=40)
	opt4=models.CharField(max_length=40)
	answer=models.CharField(max_length=40)
	
class s_payment(models.Model):
	f_name=models.CharField(max_length=40)
	email=models.CharField(max_length=40)
	mobile=models.BigIntegerField(null= True)
	
