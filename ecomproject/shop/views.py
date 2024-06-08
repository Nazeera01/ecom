
from django.shortcuts import render, get_object_or_404


from .models import Product,Category

# Create your views here.
def home(requests,slug_c=None):
    page_c=None
    products=None
    if slug_c !=None:
        page_c=get_object_or_404(Category, slug=slug_c)
        products=Product.objects.all().filter(category=page_c,available=True)
    else:
        products=Product.objects.all().filter(available=True)

    return render(requests, 'home.html',{'category':page_c,'products':products})

def prod_det(requests,slug_c,slug_p):
    try:
        product=Product.objects.get(category__slug=slug_c, slug=slug_p)

    except Exception as e:
        raise e
    return render(requests,'product.html',{'product':product})



def contact(requests):
    return render(requests, 'contact.html'),

def about(requests):
    return render(requests, 'about.html')

def base(requests):
    return render(requests, 'base.html')






