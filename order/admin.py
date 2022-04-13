from django.contrib import admin

from order.models import Order



class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','cart','shipping_address']
# Register your models here.
admin.site.register(Order)