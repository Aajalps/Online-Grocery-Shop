import datetime
from datetime import datetime
from django.shortcuts import render,redirect
from AdminApp.models import categorydb,productdb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from WebApp.models import contactdb,regdb,CartDb,Orderdb
from django.contrib import messages


# Create your views here.
def index(req):
    categories=categorydb.objects.count()
    date=datetime.now()
    products=productdb.objects.count()

    return render(req,"Index.html",{'categories':categories,'products':products,'date':date})

def add_category(req):
    return render(req,"AddCategory.html")

def save_category(req):
    if req.method=='POST':
        na=req.POST.get('category')
        de=req.POST.get('description')
        im=req.FILES.get('image')
        obj=categorydb(Category_name=na,Description=de,Image=im)
        obj.save()
        messages.success(req,"Category saved successfully")
        return redirect(add_category)


def displaying_category(req):
    data=categorydb.objects.all()
    return render(req,"DisplayingCategory.html",{'data':data})

def Edit_category(req,pro_id):
    data=categorydb.objects.get(id=pro_id)
    return render(req,"EditCategory.html",{'data':data})

def update_category(req,pro_id):
    if req.method == "POST":
        na = req.POST.get('category')
        de = req.POST.get('description')
        try:
            im = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(im.name, im)
        except MultiValueDictKeyError:
            file = categorydb.objects.get(id=pro_id).Image
        categorydb.objects.filter(id=pro_id).update(Category_name=na,Description=de,Image=file)
        messages.success(req,"Category Updated successfully")

        return redirect(displaying_category)

def delete_category(req,pro_id):
    data=categorydb.objects.filter(id=pro_id)
    data.delete()
    messages.error(req, 'Deleted Successfully')

    return redirect(displaying_category)


def add_product(req):
    category=categorydb.objects.all()
    return render(req,"AddProducts.html",{'category':category})

def save_product(req):
    if req.method=='POST':
        ca=req.POST.get('category')
        pa=req.POST.get('product')
        pr=req.POST.get('price')
        des=req.POST.get('description')
        qu=req.POST.get('quantity')
        im=req.FILES.get('image')
        obj=productdb(Category_name=ca,Product_name=pa,Price=pr,Description=des,Quantity=qu,Image=im)
        obj.save()
        messages.success(req,"Product saved successfully")

        return redirect(add_product)

def displaying_products(req):
    data=productdb.objects.all()
    return render(req,"DisplayingProducts.html",{'data':data})

def Edit_products(req,pro_id):
    category = categorydb.objects.all()
    data=productdb.objects.get(id=pro_id)
    return render(req,"EditProducts.html",{'data':data,'category':category})

def update_product(req,pro_id):
    if req.method == "POST":
        ca = req.POST.get('category')
        pa = req.POST.get('product')
        pr = req.POST.get('price')
        des = req.POST.get('description')
        qu = req.POST.get('quantity')
        try:
            im = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(im.name, im)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=pro_id).Image
        productdb.objects.filter(id=pro_id).update(Category_name=ca,Product_name=pa,Price=pr,Description=des,Quantity=qu,Image=file)
        messages.success(req,"Product Updated successfully")

        return redirect(displaying_products)

def delete_products(req,pro_id):
    data=productdb.objects.filter(id=pro_id)
    data.delete()
    messages.error(req, "Deleted successfully")

    return redirect(displaying_products)

def admin_login_page(req):
    return render(req,'AdminLogin.html')

def admin_login(request):
    if request.method=='POST':
        us=request.POST.get('username')
        pa=request.POST.get('password')
        if User.objects.filter(username_contains=us).exists():
            x=authenticate(username=us,password=pa)
            if x is not None:
                login(request,x)
                request.session['username']=us
                request.session['password']=pa
                messages.success(request, "Succesfully Login")

                return redirect(index)

            else:
                messages.warning(request, "Invalid Password")

                return redirect(admin_login_page)
        else:
            messages.warning(request, "Invalid Username")

            return redirect(admin_login_page)


def delete_logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Succesfully Login")

    return redirect(admin_login_page)


def displaying_contact(request):
    data=contactdb.objects.all()
    return render(request,'DisplayingContact.html',{'data':data})

def delete_contact(request,pro_id):
    data=contactdb.objects.filter(id=pro_id)
    data.delete()
    return redirect(displaying_contact)

def displaying_user(request):
    data=regdb.objects.all()
    return render(request,"DisplayingUser.html",{'data':data})

def delete_user(request,pro_id):
    data=regdb.objects.filter(id=pro_id)
    data.delete()
    return redirect(displaying_user)

def display_order(request):
    data = CartDb.objects.all()
    return render(request,"Display_Order.html",{'data':data})

def delete_order(request,pro_id):
    data=CartDb.objects.filter(id=pro_id)
    data.delete()
    return redirect(display_order)

def display_order2(request):
    data = Orderdb.objects.all()
    return render(request,"Display_Order2.html",{'data':data})

def delete_order2(request,pro_id):
    data=Orderdb.objects.filter(id=pro_id)
    data.delete()
    return redirect(display_order2)