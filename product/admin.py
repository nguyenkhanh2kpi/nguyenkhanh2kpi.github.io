from itertools import product
from unicodedata import category
from django.contrib import admin

from product.models import Category, Product, Variation




class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price','category','active','images']

    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','description','active']

    
class VariationAdmin(admin.ModelAdmin):
    list_display = ['product','price','sale_price']
# Register your models here.
admin.site.register(Product, ProductAdmin)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Variation, VariationAdmin)