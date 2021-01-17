 
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory #
from django.contrib import messages #сообщения об ошибках или иной информации
from django.contrib.auth import login, authenticate, logout 


from .models import *
from .forms import OrderForm, CreateUserForm
from .filters import OrderFilter

def registerPage(request):
    'Создание регистрации пользователя'
    if request.user.is_authenticated:
    		return redirect('home')
    register_form = CreateUserForm()
    if request.method == 'POST':
        register_form = CreateUserForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            user = register_form.cleaned_data.get('username')
            messages.success(request, user + ', Вы успешно зарегистрировались!')

            return redirect('login')
    context = {'register_form': register_form}
    return render(request, 'accounts/register.html', context = context)

def loginPage(request):
    if request.user.is_authenticated:
    		return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('username')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    context = {}
    return render(request, 'accounts/login.html', context=context)


def logoutUser(request):
    logout(request)
    return redirect('login')    

def home(request):
    'Главная страница'

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
    'Показать товары'

    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})


def customer(request, primary_key):
    'Показать покупателей'

    customer = Customer.objects.get(id=primary_key)
    orders = customer.order_set.all()
    total_order = orders.count()
    myfilter = OrderFilter(request.GET, queryset=orders)
    orders = myfilter.qs
    context = {'customer': customer, 'orders': orders, 'total_order': total_order, 'myfilter': myfilter}
    return render(request, 'accounts/customer.html', context=context)


def create_order(request, primary_key):
    'Создание формы заказа'

    # inlineformset_factory(Parent model, Child model, fields=Какие поля из дочерней модели разрешено выводить в форму)
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'))
    customer = Customer.objects.get(id=primary_key)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    # queryset = Order.objects.none(),
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
        form = OrderForm(request.POST, instance = form)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {'form_order': form}

    return render(request, 'accounts/order_form.html', context=context)


def delete_order(request, primary_key):
    'Удалить заказ'

    order = Order.objects.get(id = primary_key)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    
    context = {'order': order}

    return render(request, 'accounts/delete.html', context)
