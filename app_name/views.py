import stripe

from django.urls import reverse


from django.conf import settings

from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.template import loader

from django.contrib import messages

from django.contrib.auth.models import User

from .models import c_job

from .models import quiz

from .models import sp_news


@login_required(login_url='login')
# Create your views here.


def firstpage(request):
	return render(request,"index.html",{})

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_checkout_session(request):
    # Create a new Checkout Session
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'inr',
                    'product_data': {
                        'name': 'Your Product Name',
                    },
                    'unit_amount': 1000,  # Amount in cents
                },
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('success')),
        cancel_url=request.build_absolute_uri(reverse('cancel')),
    )

    return redirect(session.url)

from .models import s_payment 

def success(request):
	if request.method=='POST':
		uname=request.POST.get('username')
		email=request.POST.get('email')
		mobile=request.POST.get('mobile')
		dbs = s_payment(f_name=uname, email=email, mobile=mobile)
		dbs.save()
		return render(request, 'index.html')

	else:
		return render(request, 'success.html')

def cancel(request):
    return render(request, 'cancel.html')


from django.contrib.auth.models import User

def forget(request):
	if request.method=='POST':
		u1=request.POST.get('email')
		u2=request.POST.get('new_password')
		u= User.objects.get(email=u1)
		u.set_password(u2) 
	return render(request,"forget.html",{})


def quiz_1(request,id):
	dbs_11= quiz.objects.all()[:1]
	dbs_12=quiz.objects.all()[1:2]
	dbs_13=quiz.objects.all()[2:3]
	dbs_14=quiz.objects.all()[3:4]
	dbs_15= quiz.objects.all()[4:5]
	dbs_16=quiz.objects.all()[5:6]
	dbs_17=quiz.objects.all()[6:7]
	dbs_18=quiz.objects.all()[7:8]
	dbs_19= quiz.objects.all()[8:9]
	dbs_20=quiz.objects.all()[9:10]

	template=loader.get_template('quzi.html')
	context={
	'mymembers':dbs_11,
	'mymembers_1':dbs_12,
	'mymembers_2':dbs_13,
	'mymembers_3':dbs_14,
	'mymembers_4':dbs_15,
	'mymembers_5':dbs_16,
	'mymembers_6':dbs_17,
	'mymembers_7':dbs_18,
	'mymembers_8':dbs_19,
	'mymembers_9':dbs_20,
	}
	#return render(request,"books.html",{'dbss':dbs,'row_2':row_2,'row_3':row_3,'row_4':row_4})
	return HttpResponse(template.render(context,request))
	# return render(request,"jobs.html",{})

def r_quiz(request):
	return render(request,"quiz_result.html",{})

def jobs(request):
	dbs= c_job.objects.all()
	print(dbs)
	template=loader.get_template('jobs.html')
	context={
	'mymembers':dbs,
	}
	#return render(request,"books.html",{'dbss':dbs,'row_2':row_2,'row_3':row_3,'row_4':row_4})
	return HttpResponse(template.render(context,request))
	# return render(request,"jobs.html",{})

def news(request):
	dbs_1= sp_news.objects.all()
	print(dbs_1)
	template=loader.get_template('news.html')
	context={
	'mymembers_1':dbs_1,
	}
	#return render(request,"books.html",{'dbss':dbs,'row_2':row_2,'row_3':row_3,'row_4':row_4})
	return HttpResponse(template.render(context,request))
	# return render(request,"jobs.html",{})

from .models import registration 

def singup(request):
	if request.method=='POST':
		uname=request.POST.get('username')
		email=request.POST.get('email')
		pass1=request.POST.get('password1')
		pass2=request.POST.get('cpassword')
		address=request.POST.get('address')
		mobile=request.POST.get('mobile')
		gender=request.POST.get('gender')
		state=request.POST.get('state')
		if User.objects.filter(email=email).exists():
			messages.warning(request,'email is already exists!')
			return redirect(SignupPage)
		elif pass1!=pass2:
			messages.warning(request,'password and confirm password does not match !')
			return redirect(SignupPage)
		else:
			dbs = registration(name=uname, email=email, password=pass1, cpassword=pass2, address=address, mobile=mobile, gender=gender, state=state)
			dbs.save()
			my_user = User.objects.create_user(uname,email,pass1)
			my_user.save()
				
			return redirect('../u_login')
	return render(request,"signup.html",{})

from django.contrib.auth import login as auth_login

def user_login(request):
	if request.method=='POST':
		username=request.POST.get('username')
		pass1=request.POST.get('password1')
		user=authenticate(request,username=username,password=pass1)
		if user is not None:
			login(request,user)
			return redirect('index/')
		else:
			#return HttpResponse("username and password incoreect !!")
			return redirect('../u_login')
	return render(request,'login.html')	

def LogoutPage(request):
	logout(request)
	return redirect('../u_login')

from .models import contact 

def contact_data(request):
	if request.method=='POST':
		uname=request.POST.get('u_name')
		email=request.POST.get('email')
		mobile=request.POST.get('mobile')
		message=request.POST.get('mess')
		db = contact(c_name=uname, email=email, mobile=mobile, messages=message)
		db.save()
		return render(request,"index.html",{})
	else:
		return render(request,"contact.html",{})

def about(request):
	return render(request,"about.html",{})
