from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import AddProductForm


def home_view(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/home.html', context)


def contacts_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        return HttpResponse(f'Спасибо, {name}! Ваше сообщение получено.')
    return render(request, 'catalog/contacts.html')


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'catalog/detail.html', context)

def product_create_view(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog:home')
    else:
        form = AddProductForm()

    return render(request, 'catalog/form_add_product.html', {'form': form})
