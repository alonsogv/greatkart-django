from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()

    context = {
            'products': products,
            'product_count': product_count
        }
    

    return render(request, 'store/store.html', context=context)

def product_detail(request, category_slug, product_slug):
    try:
        #Get a single Product by doing the following: inside all the Products, get access to the category, and inside the category, get access to the slug of it
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    context = {
        'single_product': single_product
    }

    return render(request, 'store/product_detail.html', context=context)
