from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Product,Contact,Registration
from math import ceil
import json
from collections import defaultdict
from django.views.decorators.csrf import csrf_exempt
# from media.PayTm import Checksum
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password 
from paytmchecksum import PaytmChecksum
from django.http import HttpResponse
# Create your views here.
def index(request):    
    allProds =  []
    products = Product.objects.all()[:6]  # Assuming this fetches all product data

    n = len(products)
    nSlides = ceil(n / 3)  # Adjust slide calculation if necessary
    for i in range(0, n, 3):  # Break products into chunks of 4
        allProds.append(products[i:i+3])

    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)

def searchMatch(query,item):
    '''return true only if query matches the item'''
    if query in item.desc.lower() or query in item.name  or query in item.category.lower():
        return True
    else:       
        return False 

def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods }
    for cat in cats:
        prodtemp=Product.objects.filter(category=cat)
        prod= [item for item in prodtemp if searchMatch (query,item )]
        n= len(prod)
        nsalides=n//4 + ceil((n/4)-(n//4))
        if len(prod)!= 0:
           allProds.append([prod,range(1,nsalides),nsalides])
    params = {'allProds':allProds,"msg":""}
    if len(allProds) == 0 or len(query)<4:
        params = {'msg':"Please make sure to enter relevant search Query"}
    return render(request, 'shop/search.html', params)   

def product(request):
    allProds = []  # To store the final output
    products_by_category = defaultdict(list)  # To group products by category

    products = Product.objects.all()  # Fetch all product data

    # Group products by category
    for product in products:
        products_by_category[product.category].append(product)

    print("Grouped Products:", products_by_category)  # Debugging

    # Prepare data for category-wise display
    for category, products in products_by_category.items():
        n = len(products)
        nslides = ceil(n / 3)  # Calculate the number of slides per category
        chunks = [products[i:i+3] for i in range(0, n, 3)]  # Break products into chunks of 3
        allProds.append({'category': category, 'products': chunks})

    params = {'allProds': allProds}
    print("Params Data:", params)  # Debugging

    return render(request, 'shop/product.html', params)
    #  return HttpResponse("this is the about")
def about(request):
    return render(request, 'shop/about.html')
    # return HttpResponse("this is the about")

def contact(request):
    if request.method=="POST":
      
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        Phone=request.POST.get('Phone','')
        message=request.POST.get('message','')
        print(name ,email,Phone,message)
        contact= Contact(name=name,email=email,Phone=Phone,message=message)
        contact.save()
        thank =True
        return render(request,'shop/contact.html',{'thank':thank})
    return render(request,'shop/contact.html')

# def searchMatch(query,item):
#     '''return true only if query matches the item'''
#     if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
#         return True
#     else:       
#         return False 

# def search(request):
#     query = request.GET.get('search')
#     allProds = []
#     catprods=Product.objects.values('category','id')
#     cats={item['category'] for item in catprods }
#     for cat in cats:
#         prodtemp=Product.objects.filter(category=cat)
#         prod= [item for item in prodtemp if searchMatch (query,item )]
#         n= len(prod)
#         nsalides=n//4 + ceil((n/4)-(n//4))
#         if len(prod)!= 0:
#            allProds.append([prod,range(1,nsalides),nsalides])
#     params = {'allProds':allProds,"msg":""}
#     if len(allProds) == 0 or len(query)<4:
#         params = {'msg':"Please make sure to enter relevant search Query"}
#     return render(request, 'shop/search.html', params)

def productView(request ,myid):
    #Fetch the  product using the Id 
    product = Product.objects.filter(id=myid)# Fetch or return 404 if not found
    return render(request, 'shop/productview.html', {'product': product[0]})


def checkout(request):
    return HttpResponse("this is the checkout")

def handlerequest(request):
    return HttpResponse("this is the handlerequest")

def login(request):
     if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            # Fetch the user by email
            user = Registration.objects.get(email=email)

            # Check if the password matches
            if check_password(password, user.password):
                # Redirect to home or success page if login is successful
                return redirect('home')  # Replace 'home' with your actual success URL
            else:
                return HttpResponse("Invalid password. Please try again.")
        
        except Registration.DoesNotExist:
            # Handle the case when the user is not found
            return HttpResponse("User does not exist. Please register.")

    # For GET requests, render the login form
     return render(request, 'shop/login.html')
    
def register(request): 
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('Phone')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        Country = request.POST.get('Country')
        if password == cpassword:
           hashed_password = make_password(password)
           registration = Registration(name=name, email=email, Phone=phone, address=address, gender=gender, password=hashed_password, cpassword=hashed_password,Country=Country)
           registration.save()
           return redirect('login')
   
       
        else:
            # If passwords do not match, return an error message
            return HttpResponse("Password and Confirm Password don't match.")
            

    # If GET request, render the registration form
    return render(request, 'shop/Registered.html')

def Certifications(request):
    return render (request,'shop/Certifications.html')
