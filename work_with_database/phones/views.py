from django.shortcuts import render
from .models import Phone


def show_catalog(request):
    template = 'catalog.html'

    sort = request.GET.get('sort')
    catalog = Phone.objects.all()
    if sort == 'name':
        catalog = Phone.objects.order_by("name")
    elif sort == 'min_price':
        catalog = Phone.objects.order_by("price")
    elif sort == 'max_price':
        catalog = Phone.objects.order_by("-price")

    context = {'catalog': catalog}

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    
    phone = Phone.objects.get(slug=slug)

    context = {
        'phone': phone
    }
    return render(request, template, context)
