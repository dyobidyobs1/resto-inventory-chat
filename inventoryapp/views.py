from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import *
from .forms import *

def Register(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get("username")
                messages.success(request, "Account Created For " + user)
                return redirect("login")

    context = {"register": form}
    return render(request, "inventoryapp/register.html", context)

def Login(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect("index")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                messages.info(request, "Username or Password is Incorrect")

    context = {}
    return render(request, "inventoryapp/login.html")


def Logout(request):
    logout(request)
    return redirect("index")

def index(request):
    context = {}
    if request.user.is_staff == True:
        return render(request, 'inventoryapp/welcome_admin.html', context)
    else:
        return render(request, 'inventoryapp/index.html', context)



def about(request):
    context = {}
    return render(request, 'inventoryapp/about.html', context)

def contact(request):
    context = {}
    return render(request, 'inventoryapp/contact.html', context)

@login_required(login_url="login")
def inventory(request):
    stocks = FoodInventory.objects.all()
    context = {"stocks": stocks}
    return render(request, "inventoryapp/stocks.html", context)

@login_required(login_url="login")
def createstock(request):
    stockform = StockForm()
    if request.method == 'POST':
        stockform = StockForm(request.POST, request.FILES)
        if stockform.is_valid():
            stockform.save()
            print("valid")
        return redirect("inventory")
    else:
        default_subject = Branch.objects.get(id=1)
        default_type = ProdType.objects.get(id=1)
        default_size = Size.objects.get(id=1)
        # Set the default value
        stockform = StockForm(initial={
            "branch":default_subject,
            "prod_type":default_type, 
            "size":default_size
            })
    context = {'form': stockform}
    return render(request, "inventoryapp/createstock.html", context)


@login_required(login_url="login")
def updatestock(request, pk):
    post = FoodInventory.objects.get(id=pk)
    stockform = StockForm(instance=post)

    if request.method == 'POST':
        stockform = StockForm(request.POST, request.FILES, instance=post)
        if stockform.is_valid():
            stockform.save()
            return redirect('inventory')
    return render(request, 'inventoryapp/updatestock.html', {'form': stockform})

@login_required(login_url="login")
def deletestock(request, pk):
    stock = FoodInventory.objects.get(id=pk)
    if request.method == 'POST':
        stock.delete()
        return redirect('inventory')
    return render(request, 'inventoryapp/deletestock.html', {'form': stock})


@login_required(login_url="login")
def sales(request):
    sales = DailySales.objects.all()
    context = {"sales": sales}
    return render(request, "inventoryapp/sales.html", context)

@login_required(login_url="login")
def createsales(request):
    salesform = SalesForm()
    if request.method == 'POST':
        salesform = SalesForm(request.POST, request.FILES)
        if salesform.is_valid():
            salesform.save(commit=False).user = request.user
            salesform.save()
        return redirect("sales")
    context = {'form': salesform}
    return render(request, "inventoryapp/createsales.html", context)


@login_required(login_url="login")
def updatesales(request, pk):
    post = DailySales.objects.get(id=pk)
    salesform = SalesForm(instance=post)

    if request.method == 'POST':
        salesform = SalesForm(request.POST, request.FILES, instance=post)
        if salesform.is_valid():
            salesform.save()
            return redirect('sales')
    return render(request, 'inventoryapp/updatesales.html', {'form': salesform})

# def deletesales(request, pk):
#     post = Post.objects.get(rndid=pk)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('index')
#     return render(request, 'post/delete.html', {'post': post})


@login_required(login_url="login")
def adminpage(request):
    return HttpResponseRedirect(reverse('admin:index'))

@login_required(login_url="login")
def ordermenu(request):
    context = {}
    return render(request, 'inventoryapp/order_menu.html', context)


