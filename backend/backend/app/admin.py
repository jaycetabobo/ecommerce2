from django.contrib import admin
from .models import Customer, Seller, Store, Product, Order, Category
# Register your models here.

admin.site.register(Customer)
admin.site.register(Seller)
admin.site.register(Store)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Category)

