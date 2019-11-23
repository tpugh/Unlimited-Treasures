from django.shortcuts import render
from .models import Product


def index(request):
    """View function for home page of site"""
    all_products = Product.objects.all()
    context = {
            'all_products': all_products

    }
    return render(request, 'index.html', context=context) 
class catalogView(generic.ListView):
    """View function for items in the catlog"""
    model = Product
    

    
