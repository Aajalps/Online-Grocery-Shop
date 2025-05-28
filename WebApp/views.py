
from django.shortcuts import render,redirect
import razorpay
from AdminApp.models import categorydb,productdb
from WebApp.models import contactdb,regdb,CartDb,Orderdb
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User


# Create your views here.

def homePage(request):
    categories=categorydb.objects.all()
    cat_data=CartDb.objects.filter(Username=request.session['Username'])
    cat=cat_data.count()
    return render(request,"Home.html",{'categories':categories,'cat':cat})

def aboutpage(request):
    categories = categorydb.objects.all()
    cat_data = CartDb.objects.filter(Username=request.session['Username'])
    cat = cat_data.count()

    return render(request,"About.html",{'categories':categories,'cat':cat})

def contactpage(request):
    categories = categorydb.objects.all()
    cat_data = CartDb.objects.filter(Username=request.session['Username'])
    cat = cat_data.count()

    return render(request,"Contact.html",{'categories':categories,'cat':cat})

def save_contact(request):
    if request.method=='POST':
        na=request.POST.get('name')
        em=request.POST.get('email')
        nu=request.POST.get('number')
        su=request.POST.get('subject')
        me=request.POST.get('message')
        obj=contactdb(Name=na,Email=em,Number=nu,Subject=su,Message=me)
        obj.save()
        return redirect(contactpage)


def productpage(request):
    categories = categorydb.objects.all()
    products=productdb.objects.all()
    cat_data = CartDb.objects.filter(Username=request.session['Username'])
    cat = cat_data.count()

    return render(request,"Product.html",{'products':products,'categories':categories,'cat':cat})


def filtered_product(request,cat_name):

    categories = categorydb.objects.all()
    products = productdb.objects.all()
    cat_data = CartDb.objects.filter(Username=request.session['Username'])
    cat = cat_data.count()

    pro=productdb.objects.filter(Category_name=cat_name)
    return render(request,"FilteredProduct.html",{'products':products,'categories':categories,'pro':pro,'cat':cat})



def single_product(request,pro_id):
    products = productdb.objects.all()
    cat_data = CartDb.objects.filter(Username=request.session['Username'])
    cat = cat_data.count()

    data=productdb.objects.get(id=pro_id)
    return render(request,'SingleProduct.html',{'data':data,'products':products,'cat':cat})


def user_reg(request):
    return render(request,'user_registration.html')

def user_log(request):
    return render(request,'user_login.html')


def save_reg(req):
    if req.method=='POST':
        us=req.POST.get('username')
        em=req.POST.get('email')
        mb=req.POST.get('mobile')
        pa=req.POST.get('password')
        co=req.POST.get('confirm')
        obj=regdb(Username=us,Email=em,Mobile=mb,Password=pa,Confirm_password=co)
        if regdb.objects.filter(Username=us).exists():
            messages.warning(req,"User already exists...!")
            return redirect(user_reg)
        elif regdb.objects.filter(Email=em).exists():
            messages.warning(req, "Email address already exists...!")
            return redirect(user_reg)
        obj.save()
        messages.success(req,"Registered Successfully...!")
        return redirect(user_reg)

def user_login(request):
    if request.method=='POST':
        us=request.POST.get('username')
        pa=request.POST.get('password')
        if regdb.objects.filter(Username=us,Password=pa).exists():
            request.session ['Username']=us
            request.session ['Password']=pa
            messages.success(request,"Welcome to BigMart")
            return redirect(homePage)
        else:
            messages.warning(request,"Invalid Password")
            return redirect(user_reg)
    else:
        messages.warning(request, "Invalid Username")

        return redirect(user_reg)


def delete_user(request):
    del request.session['Username']
    del request.session['Password']
    messages.success(request, "Logout Successfully")

    return redirect(user_reg)


def cart(request):
    categories = categorydb.objects.all()
    cat_data = CartDb.objects.filter(Username=request.session['Username'])
    cat = cat_data.count()



    prod=CartDb.objects.filter(Username=request.session['Username'])
    sub_total=0
    shipping_charge=200

    for i in prod:
        sub_total+=i.Totalprice

    if sub_total>1000:
        shipping_charge=100
    else:
        shipping_charge=200
    Total =sub_total+shipping_charge
    return render(request,'Cart.html',{'prod':prod,'categories':categories,'sub_total':sub_total,'shipping_charge':shipping_charge,'Total':Total,'cat':cat})


def save_cart(request):
    if request.method=='POST':
        pn=request.POST.get('pname')
        qu=request.POST.get('quantity')
        pr=request.POST.get('price')
        to=request.POST.get('total')
        us=request.POST.get('username')

        try:
            x=productdb.objects.get(Product_name=pn)
            img=x.Image

        except productdb.DoesNotExist:
            img=None
        obj=CartDb(Username=us,Product_Name=pn,Quantity=qu,Price=pr,Totalprice=to,Image=img)
        obj.save()
        messages.success(request, "Added to Cart...!")
        return redirect(homePage)


def delete_Cart(request,pro_id):
    data=CartDb.objects.filter(id=pro_id)
    data.delete()
    messages.success(request, "Delete Cart Product...!")
    return redirect(cart)


def checkout(request):
    cat_data = CartDb.objects.filter(Username=request.session['Username'])
    cat = cat_data.count()

    sub_total=0
    shipping_charge=0
    prod=CartDb.objects.filter(Username=request.session['Username'])
    for i in prod:
        sub_total+=i.Totalprice
    if sub_total>1000:
        shipping_charge=100
    else:
        shipping_charge=200
    Total=sub_total+shipping_charge

    return render(request,'Checkout.html',{'prod':prod,'sub_total':sub_total,'shipping_charge':shipping_charge,'Total':Total,'cat':cat})



def save_bill(request):
    if request.method=='POST':
        na=request.POST.get('name')
        em=request.POST.get('email')
        pl=request.POST.get('place')
        ad=request.POST.get('address')
        mo=request.POST.get('mobile')
        st=request.POST.get('state')
        pi=request.POST.get('pin')
        to=request.POST.get('total')
        me=request.POST.get('message')
        obj=Orderdb(Name=na,Email=em,Place=pl,Address=ad,Mobile=mo,State=st,Pin=pi,TotalPrice=to,Messages=me)
        obj.save()
        return redirect(payment)

def payment(request):
    customer=Orderdb.objects.order_by('-id').first()


    payy=customer.TotalPrice

    amount=int(payy*100)

    payy_str=str(amount)

    if request.method=='POST':
        order_currency="INR"
        client=razorpay.Client(auth=('rzp_test_ObJHmffMu9mQKT','KmoRNiyfvcOWpIYspY3pikVV'))
        payment=client.order.create({'amount':amount,'currency':order_currency})
    return render(request,'Payment.html',{'customer':customer,'payy_str':payy_str})

