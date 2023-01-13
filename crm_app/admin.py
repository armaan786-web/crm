from django.contrib import admin
from . models import *
from django.contrib.admin.options import ModelAdmin

# Register your models here.

class ProductAdmin(ModelAdmin):
    list_display = ["name","price","description","duration","commission","product_img"]


admin.site.register(Profile)
admin.site.register(Prodcut,ProductAdmin)
admin.site.register(upi)
admin.site.register(recharge)
admin.site.register(kyc)
admin.site.register(Booking)

