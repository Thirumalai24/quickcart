from django.shortcuts import render, redirect, HttpResponse
from . models import *
from shop.form import CustomUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

#Home page
def home(request):
    products=Product.objects.filter(trending=1)
    return render(request,"shop/index.html",{"products":products})

#User Register
def register(request):
    form = CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registeration Success")
            return redirect('/login')
    return render(request,"shop/register.html",{"form":form})

#login
def login_page(request):
  if request.user.is_authenticated:
    return redirect("/")
  else:
    if request.method=='POST':
      name=request.POST.get('username')
      pwd=request.POST.get('password')
      user=authenticate(request,username=name,password=pwd)
      if user is not None:
        login(request,user)
        messages.success(request,"Logged in Successfully")
        return redirect("/")
      else:
        messages.error(request,"Invalid User Name or Password")
        return redirect("/login")
    return render(request,"shop/login.html")

#logout
def logout_page(request):
  if request.user.is_authenticated:
    logout(request)
    messages.success(request,"Logged out Successfully")
  return redirect("/")

#Products All Category
def collections(request):
    category = Category.objects.filter(status=0)
    return render(request,"shop/collections.html",{"category": category})

#Products Selected Category
def collectionsview(request,name):
    if(Category.objects.filter(name=name,status=0)):
        products=Product.objects.filter(category__name = name)
        return render(request,"shop/products/index.html",{"products": products,"category_name": name})
    else:
        messages.warning(request,"No Such products found")
        return redirect('collections')

#Selcted Product details
def product_details(request,cname,pname):
    if(Category.objects.filter(name=cname,status=0)):
        if(Product.objects.filter(name=pname,status=0)):
            products=Product.objects.filter(name=pname,status=0).first()
            return render(request,"shop/products/product_details.html",{"products":products})
        else:
            messages.error(request,"No Such products found")
            return redirect('collections')
    else:
        messages.error(request,"No Such products found")
        return redirect('collections')
