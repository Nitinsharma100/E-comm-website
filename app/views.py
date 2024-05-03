from django.shortcuts import render
from app.models import Contact
from django.contrib import messages

def home(request):
 return render(request, 'app/home.html')

def product_detail(request):
 return render(request, 'app/productdetail.html')

def product2(request):
    return render(request,'app/product2.html')

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

def login(request):
 return render(request, 'app/login.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        contact=Contact(name=name,email=email   ,phone=phone,password=password,confirm_password=confirm_password)
        contact.save()
        messages.success(request, "Your message has been submitted successfully")
    return render(request,'app/contact.html')


def checkout(request):
 return render(request, 'app/checkout.html')

def laptop(request):
 return render(request, 'app/laptop.html')

def women(request):
    return render(request,'app/women.html')



def men(request):
    return render(request,'app/men.html')