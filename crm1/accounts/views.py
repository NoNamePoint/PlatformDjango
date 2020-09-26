from django.shortcuts import render
from django.http import HttpResponse


from .models import *


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_orders = orders.count()
    total_customers = customers.count()
    delivered = orders.filter(status='Доставлено').count()
    total_pendings = orders.filter(status='Ожидание').count()

    context = {'orders': orders, 'customers': customers, "total_customers": total_customers,
               'total_orders': total_orders, 'total_pendings': total_pendings, 'delivered': delivered}

    return render(request, 'accounts/dashboard.html', context=context)


def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})


def customer(request, primary_key):
    customers = Customer.objects.get(id=primary_key)
    order = customers.order_set.all()
    context = {'customers': customers, 'order': order}
    return render(request, 'accounts/customer.html', context=context)
	



