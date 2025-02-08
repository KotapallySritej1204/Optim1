from django.contrib import admin
from .models import *

class VendorAdmin(admin.ModelAdmin):
    list_display=['store_name']
class ProductAdmin(admin.ModelAdmin):
    list_display=['vendor','title','price']
class OrderAdmin(admin.ModelAdmin):
    list_display=['product','timestamp']


admin.site.register(Vendor,VendorAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)
