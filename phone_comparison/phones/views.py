from django.shortcuts import render
from .models import Phone, Apple, Samsung

def show_catalog(request):
    template = 'catalog.html'
    context = {
        'Phones': Phone.objects.all(),
        'Additional': [
            Apple.objects.first(),
            Samsung.objects.first(),
        ]
    }
    
    return render(
        request,
        template,
        context
    )
