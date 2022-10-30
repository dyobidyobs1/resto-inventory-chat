from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'inventoryapp/index.html', context)

def about(request):
    context = {}
    return render(request, 'inventoryapp/about.html', context)

def contact(request):
    context = {}
    return render(request, 'inventoryapp/contact.html', context)