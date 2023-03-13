from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.views import generic
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
import json
import datetime
from.utils import cookieCart, cartData ,guestOrder


from .models import *

def recreationCenters(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete =False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']
    context ={'items':items,'order':order,'cartItems': cartItems  }
    return render(request, 'VRApp/recreation.html',context)

def animalParks(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete =False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']
    context ={'items':items,'order':order,'cartItems': cartItems  }
    return render(request, 'VRApp/parks.html',context)
    
def cities(request,title):
    city = City.objects.get(title=title)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete =False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']
    context ={'items':items,'order':order,'cartItems': cartItems ,'city': city}
    return render(request,'VRApp/city.html',context)

def countries(request,title):
    country = Country.objects.get(title=title)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete =False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']
    context ={'items':items,'order':order,'cartItems': cartItems ,'country': country}
    return render(request,'VRApp/country.html',context)

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def home(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete =False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']
    context ={'items':items,'order':order,'cartItems': cartItems  }
    return render(request, 'VRApp/home.html',context)

def historicalSites(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete =False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']
    context ={'items':items,'order':order,'cartItems': cartItems  }
    return render(request, 'VRApp/historical_sites.html',context)

def shop(request):
    data = cartData(request)
    cartItems = data['cartItems']
    products = Product.objects.all()
    context ={'products':products, 'cartItems':cartItems}
    return render(request, 'VRApp/shop.html',context)


def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    context ={'items':items,'order':order,'cartItems': cartItems  }
    return render(request, 'VRApp/cart.html',context)

def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    context ={'items':items,'order':order,'cartItems':cartItems }
    return render(request, 'VRApp/checkout.html',context)
 
def updateItem(request):
    data = json.loads(request.body)
    productID =data['productID']
    action = data['action']

    print('Action:', action)
    print('ProductID', productID)
	
    customer = request.user.customer
    product = Product.objects.get(id = productID)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action =='add':
        orderItem.quantity =(orderItem.quantity + 1)
    elif action =='remove':
        orderItem.quantity =(orderItem.quantity - 1) 


    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()      
    

    return JsonResponse('Item was added', safe=False)               


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        customer , order = guestOrder(request,data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True

    order.save()  
    if order.shipping == True:
            ShippingAddress.objects.create(
                customer= customer,
                order= order,
                address = data['shipping']['address'],
                city = data['shipping']['city'],
                state = data['shipping']['state'],
                zipcode = data['shipping']['zipcode']
            )           
    return JsonResponse('Payment complete', safe=False)               


