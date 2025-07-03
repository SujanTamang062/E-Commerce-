from django.contrib import admin
from .models import Category,Product,CartItem,Order,OrderItem,Payment

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)
# Register your models here.
