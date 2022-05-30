from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *

from .forms import *

from django.forms import inlineformset_factory
from .filters import OrderFilter



def register(request):
    if request.user.is_authenticated:
        return redirect("accounts:home")
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get("username")
                messages.success(request, "User created successfully for "+user)
                return redirect(reverse("accounts:loginpage"))

        return render(request, "accounts/register.html", {
            "form": form
        })


def loginpage(request):
    if request.user.is_authenticated:
        return redirect("accounts:home")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)
        
            if user is not None:
                login(request, user)
                return redirect(reverse("accounts:home"))
            else:
                messages.info(request, "Username or password is incorrest")

        return render(request, "accounts/login.html", {
            
        })


def logoutuser(request):
    logout(request)
    return redirect(reverse("accounts:loginpage"))


@login_required(login_url="accounts:loginpage")
def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()

    total_orders = orders.count()
    orders_delivered = Order.objects.filter(status = "Delivered").count()
    orders_pending = Order.objects.filter(status = "Pending").count()

    return render(request, 'accounts/dashboard.html', {
        "orders": orders,
        "customers": customers,
        "total_orders": total_orders,
        "delivered": orders_delivered,
        "pending": orders_pending,
    })

@login_required(login_url="accounts:loginpage")
def products(request):
    products = Product.objects.all()

    return render(request, 'accounts/products.html', {
        "products": products,
    })

@login_required(login_url="accounts:loginpage")
def customer(request, pk):
    customer = Customer.objects.get(id = pk)
    total_orders = customer.order_set.all().count()
    orders = customer.order_set.all()

    myFilter = OrderFilter(request.GET, queryset = orders)
    orders = myFilter.qs

    return render(request, 'accounts/customer.html', {
        "customer": customer,
        "tot_orders": total_orders,
        "orders": orders,
        "myFilter": myFilter,
    })


@login_required(login_url="accounts:loginpage")
def create_order(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=("product", "status"), extra=6)
    customer = Customer.objects.get(pk=pk)

    # form = OrderForm(initial={"customer": customer}) 
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)

    if request.method == "POST":
        # print("post info: ", request.POST)

        # form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            print("form is valid")
            return redirect(reverse('accounts:home'))

    return render(request, 'accounts/order_form.html', {
        "formset": formset
    })


@login_required(login_url="accounts:loginpage")
def update_order(request, pk):
    order = Order.objects.get(pk=pk)
    form = OrderForm(instance=order)

    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:home'))

    return render(request, 'accounts/order_form.html', {
        "formset": form
    })


@login_required(login_url="accounts:loginpage")
def delete_order(request, pk):
    order = Order.objects.get(pk=pk)
    
    if request.method == 'POST':
        order.delete()
        return redirect(reverse("accounts:home"))

    return render(request, 'accounts/delete_order.html', {
        "item": order
    })