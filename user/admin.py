from msilib.schema import CustomAction
from django.contrib import admin

from user.models import CustomerUser


class CustomerUserAdmin(admin.ModelAdmin):
    list_display = ['phone_number']
# Register your models here.
admin.site.register(CustomerUser)