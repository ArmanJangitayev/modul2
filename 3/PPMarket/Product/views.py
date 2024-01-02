from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ProductCategory
from .forms import ProductForm, SearchForm, ProductCategoryForm


def product_list(request):
    products = Product.objects.all()
    categories = ProductCategory.objects.all()
    return render(request, 'product_list.html', {'products': products, 'categories': categories})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('product_list')


def search_products(request):
    categories=ProductCategory.objects.all()
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            print(form.cleaned_data)
            query = form.cleaned_data['query']
            category = form.cleaned_data['category']
            min_price = form.cleaned_data['min_price']
            max_price = form.cleaned_data['max_price']
            products = Product.objects.filter(
                name__icontains=query,
                price__gte=min_price,
                price__lte=max_price,
                category=category
            )
            return render(request, 'product_list.html', {'products': products, 'categories': categories})
    else:
        form = SearchForm()
    return render(request, 'search_form.html', {'form': form})


def category_list(request):
    categories = ProductCategory.objects.all()
    return render(request, 'category_list.html', {'categories': categories})


def category_detail(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    return render(request, 'category_detail.html', {'category': category})


def category_create(request):
    if request.method == 'POST':
        form = ProductCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = ProductCategoryForm()
    return render(request, 'category_form.html', {'form': form})


def category_edit(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        form = ProductCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = ProductCategoryForm(instance=category)
    return render(request, 'category_form.html', {'form': form})


def category_delete(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)

    category.delete()
    return redirect('category_list')
