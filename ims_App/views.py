from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

# Create your views here.

# Create View
def create_view(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read')
        else:
            form = ProductForm()
    
    context = {
                'form':form,
    }
            
    return render(request, 'invTemplate/product_form.html', context)


# Read View
def read_view(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request, 'invTemplate/product_list.html', context)


# Update View
def update_view(request, product_id):
    product = Product.objects.get(product_id=product_id)
    form = ProductForm(instance=product)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('read')
        else:
            form = ProductForm(instance=product)
            
    context={
            'form':form
    }
            
    
    return render(request, 'invTemplate/product_form.html', context)

# Delete View
def delete_view(request, product_id):
    product = Product.objects.get(product_id=product_id)
    form = ProductForm(instance=product)
    if request.method=='POST':
        product.delete()
        return redirect('read')
    
    context = {
            'product':product
    }
    return render(request, 'invTemplate/product_confirm_delete.html')

# Home View

def home_view(request):
    return render(request, 'invTemplate/home.html')