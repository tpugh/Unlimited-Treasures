from django.contrib import admin
from .models import Customer, Product, OnlineStore, Cart, Payment, Order

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(OnlineStore)
admin.site.register(Cart)
admin.site.register(Payment)
admin.site.register(Order)