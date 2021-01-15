from django.shortcuts import render, redirect
from django.forms import inlineformset_factory


from .models import *
from .forms import OrderForm


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
    customer = Customer.objects.get(id=primary_key)
    orders = customer.order_set.all()
    total_order = orders.count()
    context = {'customer': customer, 'orders': orders, 'total_order': total_order}
    return render(request, 'accounts/customer.html', context=context)


def create_order(request, primary_key):
    'Контроллер для корректного создания формы заказа'
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'))
    customer = Customer.objects.get(id=primary_key)
    formset = OrderFormSet(instance=customer)
    # form = OrderForm(initial={"customer": customer})
    if request.method == 'POST':
         #Проверяем тип вызываемого метода
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/') 

    context = {'formset': formset}
    return render(request, "accounts/order_form.html", context = context)
	
def update_order(request, primary_key):
    'Обновление заказа'

    order = Order.objects.get(id=primary_key) #получаем объект заказа с заполненными полями
    form = OrderForm(instance=order) #Чтобы отразить предзаполненние данные в полях формы передаем в instance объект заказа
    if request.method == 'POST':  # Проверяем тип вызываемого метода
        # Если метод POST, то пересоздаем объект заказа с переданными в вызывающий класс данными из полей модели нового заказа
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {'form_order': form}

    return render(request, 'accounts/order_form.html', context=context)


def delete_order(request, primary_key):
    order = Order.objects.get(id = primary_key)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    
    context = {'order': order}

    return render(request, 'accounts/delete.html', context)
