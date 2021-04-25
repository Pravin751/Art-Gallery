from django.shortcuts import  get_object_or_404
from django.http import  JsonResponse
from django.shortcuts import render,redirect,reverse
from . models import *
from django.contrib.auth.models import User,auth
from django.contrib.auth import views as app_views
from django.core.mail import send_mail
from django.http import HttpResponse
from django.db.models import Q
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import  authenticate
from django.core.paginator import Paginator

 
from django.contrib import messages
def forgotpassword(request):
	if request.session.has_key('username'):
		return redirect('index')
	else:
		if request.method == 'POST':
			a = request.POST.get('email')
			user_exsit  =  register33.objects.filter(emailid=a)
			if user_exsit:
		
		
				html_message='<h1><a href="http://127.0.0.1:8000/forgotconfirm">Click</a></h1>'


				res=send_mail(
				'ppp',
				'hello',
				'agpravin2000@gmail.com',
		 		[a],
				html_message=html_message)
				return HttpResponse('Successfully emailsent')
			else:
				messages.success(request,'email does not found' )
	return render(request,'forgotpassword.html')
def forgotconfirm(request):
	if request.session.has_key('username'):
		return redirect('index')
	else:
		users = register33.objects.filter()
		if request.method == 'POST':
			a = request.POST.get('password')
			user=register33.objects.update(password=a)
	
		
		
		
			return redirect('login')
	return render(request,'forgotconfirm.html',{'users':users})		

def home(request):
	post_detail = ArtistAccount.objects.all().order_by("-id")
	cats = Category.objects.all().order_by("cat_name")
	
	
	return render(request,'home.html',{'post_detail':post_detail,'category':cats})		

def index(request):
	if request.session.has_key('username'):
		post_detail = ArtistAccount.objects.all().order_by("-id")
		cats = Category.objects.all().order_by("cat_name")
		uid = request.session['user_id']
		user = register33.objects.filter(id=int(uid))
		
		return render(request,'index.html',{'post_detail':post_detail,'user':user,'category':cats})
	else:
		return render(request,'home.html',{})
	
def user_register(request):
	cats = Category.objects.all().order_by("cat_name")
	if request.method == 'POST':
		a = request.POST.get('fname')
		b = request.POST.get('lname')
		c = request.POST.get('email')
		d = request.POST.get('username')
		e = request.POST.get('password')
		f = request.POST.get('date')
		g = request.POST.get('number')
		h = request.POST.get('content')
		
		user_exsit  =  register33.objects.filter(username=d)
		
		if user_exsit:
			messages.success(request, 'Username  already Exist.')
		
			
		else:
			user = register33.objects.create(Firstname=a,Lastname=b,emailid=c,username=d,password=e,date=f,contact_number=g,Address=h)
			if user:
				messages.success(request,'Successfully Register.')
				return redirect('login')
	return render(request,'user_register.html',{'category':cats})
		

			
	
		
def login(request):
	if request.session.has_key('username'):
		return redirect('index')
	else:
		if request.method == 'POST':
			a = request.POST.get('username')
			b = request.POST.get('password')
			user = register33.objects.filter(username=a,password=b)
			if user:
				
				request.session['username'] = a
				user_id = register33.objects.only('id').get(username=a).id
				request.session['user_id'] = user_id

				return redirect('index')
			else:
				messages.success(request,"Invalid Username or Password")
		return render(request,'login.html',{})

def change_password(request):
    context={}
    uid = request.session['user_id']
    ch = register33.objects.filter(id=int(uid))
    if len(ch)>0:
        data = register33.objects.get(id=int(uid))
        context["data"] = data
    if request.method=="POST":
        current = request.POST["cpwd"]
        new_pas = request.POST["npwd"]
        
        user = register33.objects.get(id=int(uid))
        un = user.username
        check = user.check_password(current)
        if check==True:
            user.set_password(new_pas)
            user.save()
            context["msz"] = "Password Changed Successfully!!!"
            context["col"] = "alert-success"
            user = register33.objects.get(username=un)
            login(request,user)
        else:
            context["msz"] = "Incorrect Current Password"
            context["col"] = "alert-danger"

    return render(request,"change_password.html",context)

    

def logout(request):
    auth.logout(request)
    return redirect('/')
def ArtistAccountt(request):
	if request.session.has_key('user_id'):
		category_detail = Category.objects.all()
		user_name = register33.objects.all()
		uid = request.session['user_id']
		
		if request.method == 'POST':
			a = request.POST.get('user_detail')
			b = request.FILES['picture']
			
			c = request.POST.get('price')
			d = request.POST.get('content1')
		
			e = request.POST.get('category')
			f = request.POST.get('pname')
			g = request.POST.get('pprice')
			h = request.POST.get('height')
			i = request.POST.get('Width')
			cat_id = Category.objects.get(id=int(e))
			user_id = register33.objects.get(id=int(uid))
			crt = ArtistAccount.objects.create(user_id=user_id,Category=cat_id,image=b,saleprice=c,content=d,productname=f,productprice=g,height=h,width=i)
			if crt:
				messages.success(request,'Successfully Created.')
		return render(request,'ArtistAccount.html',{'user_name':user_name,'category_detail':category_detail})
	else:
		return render(request,'login.html',{})		

def Singleproduct(request,jk):
    
    users = ArtistAccount.objects.filter(id=jk)
    cats = Category.objects.all().order_by("cat_name")
    

    
	
    
    

    return render(request,"Single product.html",{'users':users,'category':cats})

def allproduct(request):
    context = {}
    cats = Category.objects.all().order_by("cat_name")
    context["category"] = cats
    all_products = ArtistAccount.objects.all()
    
    paginator = Paginator(all_products, 1)
    page=request.GET.get('page')
    page_obj=paginator.get_page(page)
    context["products"]=all_products
    
    
    
    
    if "qry" in request.GET:
        q = request.GET["qry"]
        # p = request.GET["price"]
        prd = ArtistAccount.objects.filter(Q(productname__icontains=q)|Q(Category__cat_name__contains=q))
        # prd = add_product.objects.filter(Q(product_name__icontains=q)& Q(sale_price__lt=p))
        # prd = add_product.objects.filter(product_name__contains=q)
        context["products"] = prd   
        context["abcd"]="search"
    if "category" in request.GET:
        cid = request.GET["category"]
        prd = ArtistAccount.objects.filter(Category__id=cid)
        context["products"] = prd   
        context["abcd"]="search"

    return render(request,"all product.html",context)

def my_products(request):
	context = {}
	uid = request.session['user_id']
	user_detail = register33.objects.filter(id=int(uid))
	context["user_detail"] = user_detail
	
	all = ArtistAccount.objects.filter(user_id=int(uid)).order_by("-id")
	context["products"] = all
	
	return render(request,"my products.html",context)    

def update_product(request):
    context ={}
    cats = Category.objects.all().order_by("cat_name")
    context["category"] = cats

    pid = request.GET["pid"]
    product = get_object_or_404(ArtistAccount,id=pid)
    context["product"] = product

    if request.method=="POST":
        pn = request.POST["pname"]
        ct_id = request.POST["pcat"]
        pr = request.POST["pp"]
        sp = request.POST["sp"]
        des = request.POST["des"]
        
        cat_obj = Category.objects.get(id=ct_id)

        product.productname =pn
        product.Category =cat_obj
        product.productprice =pr
        product.saleprice =sp
        product.content =des
        if "pimg" in request.FILES:
            img = request.FILES["pimg"]
            product.image = img
        product.save()
        context["status"] = "Changes Saved Successfully"
        context["id"] = pid
    return render(request,"update_product.html",context)

def delete_product(request):
    context = {}
    if "pid" in request.GET:
        pid = request.GET["pid"]
        prd = get_object_or_404(ArtistAccount, id=pid)
        context["product"] = prd

        if "action" in request.GET:
            prd.delete()
            context["status"] = str(prd.productname)+" removed Successfully!!!"
    return render(request,"delete_product.html",context)



def cart1(request):
    context={}
    uid = request.session['user_id']
    items = cart.objects.filter(user__id=int(uid),status=False)
    context["items"] = items

    if request.session.has_key('user_id'): 
        if request.method=="POST":
            pid = request.POST["pid"]
            qty = request.POST["qty"]
            is_exist = cart.objects.filter(product__id=pid,user__id=int(uid),status=False)
            if len(is_exist)>0:
                context["msz"] = "Item Already Exists in Your Cart"
                context["cls"] = "alert alert-warning"
            else:    
                product =get_object_or_404(ArtistAccount,id=pid)
                usr = get_object_or_404(register33,id=int(uid))
                c = cart(user=usr,product=product,quantity=qty)
                c.save()
                context["msz"] = "{} Added in Your Cart".format(product.productname)
                context["cls"] = "alert alert-success"
    else:
        context["status"] = "Please Login First to View Your Cart"
    return render(request,"cart.html",context)

def get_cart_data(request):
	uid = request.session['user_id']
	items = cart.objects.filter(user__id=int(uid), status=False)
	sale,total,quantity =0,0,0
	for i in items:
		sale += float(i.product.saleprice)*i.quantity
		total += float(i.product.productprice)*i.quantity
		quantity+= int(i.quantity)

	res = {
        "total":total,"offer":sale,"quan":quantity,
    }
	return JsonResponse(res)

def change_quan(request):
    if "quantity" in request.GET:
        cid = request.GET["cid"]
        qty = request.GET["quantity"]
        cart_obj = get_object_or_404(cart,id=cid)
        cart_obj.quantity = qty
        cart_obj.save()
        return HttpResponse(cart_obj.quantity)

    if "delete_cart" in request.GET:
        id = request.GET["delete_cart"]
        cart_obj = get_object_or_404(cart,id=id)
        cart_obj.delete()
        return HttpResponse(1) 	

    
def profile33(request):
	
	uid = request.session['user_id']
	user = register33.objects.filter(id=int(uid))
	
	

	
	return render(request,'profile33.html',{'user':user})

    
def profile(request):
	if request.session.has_key('username'):
		
		a = "Profile Page"
		user_detail = Person.objects.all()
		post_detail = Post.objects.all()
	
		return render(request,'profile.html',{'b':a,'users':user_detail,
		'post_detail':post_detail})
	else:
		return render(request,'login.html',{})
def add_user(request):
	if request.method == 'POST':
		a = request.POST.get('fname')
		b = request.POST.get('lname')
		c = request.POST.get('email')
		d = request.POST.get('date')
		crt = Person.objects.create(first_name=a,last_name=b,email=c,date=d)
		if crt:
			messages.success(request,'Successfully Created.')
	return render(request,'add_user.html',{})

def add_post(request):
	
		
		user_name = Person.objects.all()
		
		post_detials = Post.objects.filter()
		if request.method == 'POST':
			a = request.POST.get('title')
			b = request.FILES['pic']
			
			c = request.POST.get('user_detail')
			d = request.POST.get('content')
			user_id = Person.objects.get(id=int(c))
			crt = Post.objects.create(user_id=user_id,title=a,content=d,picture=b)
			if crt:
				messages.success(request,'Successfully Created.')
		return render(request,'add_post.html',{'user_name':user_name})
		
def user_edit(request,pk):
	
	user = register33.objects.filter(id=pk)
	
	if request.method == 'POST':
		a = request.POST.get('fname')
		b = request.POST.get('lname')
		c = request.POST.get('email')
		d = request.POST.get('image')
		
		crt = register33.objects.filter(id=pk).update(Firstname=a,Lastname=b,emailid=c,picture=d)
		if "image" in request.FILES:
  			img = request.FILES["image"]
  			user.picture = img
  			user.save()

	
	return render(request,'user_edit.html',{'user':user})	

    



def user_delete(request,a):
	Person.objects.filter(id=a).delete()
	return redirect('profile')


from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings 


def process_payment(request):
	uid = request.session['user_id']
	items = cart.objects.filter(user_id__id=int(uid),status=False)
	products=""
	amt=0
	inv = "INV10001-"
	cart_ids = ""
	p_ids =""
	for j in items:
		products += str(j.product.productname)+"\n"
		p_ids += str(j.product.id)+","
		amt += float(j.product.saleprice)
		inv +=  str(j.id)
		cart_ids += str(j.id)+","

	paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': str(amt),
        'item_name': products,
        'invoice': inv,
        'notify_url': 'http://{}{}'.format("127.0.0.1:8000",
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format("127.0.0.1:8000",
                                           reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format("127.0.0.1:8000",
                                              reverse('payment_cancelled')),
    }
	uuid = request.session['username']

	usr = register33.objects.get(username=(uuid))
	ord = Order(cust_id=usr,cart_ids=cart_ids,product_ids=p_ids)
	ord.save()
	ord.invoice_id = str(ord.id)+inv
	ord.save()
	request.session["order_id"] = ord.id
    
	form = PayPalPaymentsForm(initial=paypal_dict)
	return render(request, 'process_payment.html', {'form': form})

def payment_done(request):
    if "order_id" in request.session:
        order_id = request.session["order_id"]
        ord_obj = get_object_or_404(Order,id=order_id)
        ord_obj.status=True
        ord_obj.save()
        
        for i in ord_obj.cart_ids.split(",")[:-1]:
            cart_object = cart.objects.get(id=i)
            cart_object.status=True
            cart_object.save()
    return render(request,"payment_success.html")




def payment_cancelled(request):
    return render(request,"payment_failed.html")    

def order_history(request):
	context = {}
	uid = request.session['user_id']
	user_detail = register33.objects.filter(id=int(uid))
	if len(user_detail)>0:
		user_detail1 = register33.objects.get(id=int(uid))
		context["user_detail1"] = user_detail1
		

	all_orders = []
	orders = Order.objects.filter(cust_id__id=int(uid)).order_by("-id")
	for order in orders:
		products = []
		for id in order.product_ids.split(",")[:-1]:
			pro = get_object_or_404(ArtistAccount, id=id)
			products.append(pro)
		ord = {
            "order_id":order.id,
            "products":products,
            "invoice":order.invoice_id,
            "status":order.status,
            "date":order.processed_on,
        }
		all_orders.append(ord)
	context["order_history"] = all_orders
	
	
	return render(request,"order_history.html",context)

def my_customer(request):
	context = {}
	uid = request.session['user_id']
	user_detail = register33.objects.filter(id=int(uid))
	if len(user_detail)>0:
		user_detail1 = register33.objects.get(id=int(uid))
		context["user_detail1"] = user_detail1
    
	products = cart.objects.filter(product_id=int(uid) ,status=True)
	cust =[]
	ids=[]
	context["times"] = len(products)
	for i in products:
		us = {
		    "username":i.user.username,
		    "Firstname":i.user.Firstname,
		    "Lastname":i.user.Lastname,
		    "emailid":i.user.emailid,
		}
		check = register33.objects.filter(id=i.user.id)
		if len(check)>0:
			prf = get_object_or_404(register33,id=i.user.id)
			us["picture"] = prf.picture
		ids.append(i.user.id)
		count = ids.count(i.user.id)
		if count<2:
			cust.append(us)
			count +=1
	context["customers"] = cust
	context["Products"] = products
	
	return render(request,"my_cust.html",context)	

def register12(request):

	return render(request,"register12.html")

def cust_dashboard(request):
    context = {}
    uid = request.session['user_id']
    check = register33.objects.filter(id=int(uid))
    if len(check)>0:
        data = register33.objects.get(id=int(uid))
        context["data"] = data
    return render(request,"cust_dashboard.html",context)

def photopainting(request):

	uid = request.session['user_id']
	cats = Category.objects.all().order_by("cat_name")
	photo = Photo.objects.filter(user_id=int(uid))

	return render(request,"My Photo.html",{'photo':photo,'category':cats})

def seller(request):
  
    if request.method=="POST":
        shopname = request.POST["sname"]
        
        un = request.POST["uname"]
        pwd = request.POST["password"]
        em = request.POST["email"]
        con = request.POST["contact"]
        tp = request.POST["utype"]
        spa = request.POST["spaddr"]
        
        usr = User.objects.create_user(un,em,pwd)
        
        if tp=="sell":
            usr.is_staff = True
            usr.save()

        reg = Selleraccount.objects.create(shop=shopname,shopaddress=spa,user=usr, contact_number=con)
        if reg:
        	messages.success(request,'Successfully Register.')
        
    return render(request,"register100.html")

def photoconvert(request):
	category_detail = Category.objects.all()
	if request.method=="POST":
		username = request.POST["uname"]
		pt = request.POST["photo"]
		ht = request.POST["height"]
		wt = request.POST["width"]
		ct = request.POST["category"]
		user = Customphoto.objects.create(user__id=username,photo=pt,Imageheight=ht,ImageWidth=wt,Category=ct)
		if user:
			messages.success(request,'Successfully Register.')

	return render(request,"customphoto.html",{'category_detail':category_detail})
        
