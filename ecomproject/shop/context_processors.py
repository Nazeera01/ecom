from .models import Product


def mylink(request):

    links=Product.objects.all()
    return dict(links=links)