from django.shortcuts import render,redirect,HttpResponse
from . models import * 
from django.contrib import messages
from shop.form import CustomUserForm
from django.contrib.auth import authenticate,login,logout

def home(request):
    Trend_showing_in_home=product.objects.filter(trending=1)
    return render(request,"shop/index.html",{"products_var":Trend_showing_in_home})

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged Out Successfully")
    return redirect('/')

def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in successfully")
                return redirect("/")
            else:
                messages.error(request,"Invalid User Name or  Password")
                return redirect("/login")
        return render(request,"shop/login.html")


def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration SuccessFull You Can Log In Now ..!")
            return redirect('/login')
    return render(request,"shop/register.html",{'form':form})

def collections(request):
    
    context={
        'catagory':catagory.objects.filter(status=0)
    }
    print(context)
    return render(request,"shop/collections.html",context)

def collectionsview(request,name):
    if(catagory.objects.filter(name=name,status=0)):
        products=product.objects.filter(catagory__name=name)
        print(products)
        return render(request,"shop/products/index.html",{"products":products,"product_name":name})

    else:
        messages.warning(request,"No Such Category Found")
        return redirect('collections')


def product_details(request,cname,pname):
    if(catagory.objects.filter(name=cname,status=0)):
        if(product.objects.filter(name=pname,status=0)):
            products=product.objects.filter(name=pname,status=0).first()
            print(products.catagory.name)
            return render (request,"shop/products/product_details.html",{"products":products})
        else:
            messages.error(request,"No Such Product Found")
            return redirect('collections')
    else:
        messages.error(request,"No Such Catagory Found")
        return redirect ('collections')