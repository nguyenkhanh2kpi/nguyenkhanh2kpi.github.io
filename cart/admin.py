from django.contrib import admin

from cart.models import Cart, CartItem


class CartAdmin(admin.ModelAdmin):
    list_display = ['user','created_at','updated_at']

    
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart','item','quantity']

# Register your models here.
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)