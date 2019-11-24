from django.shortcuts import render, get_object_or_404
from .models import Product, Item, OrderItem, Order, Address, Payment, Coupon, Refund, UserProfile
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from django.shortcuts import redirect
from django.utils import timezone
from .forms import CheckoutForm, CouponForm, RefundForm, PaymentForm



def index(request):
    """View function for home page of site"""
    all_products = Product.objects.all()
    context = {
            'all_products': all_products

    }
    return render(request, 'index.html', context=context) 
