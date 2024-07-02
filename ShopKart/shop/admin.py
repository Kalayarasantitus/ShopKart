from django.contrib import admin
from .models import *

class catagoryAdmin(admin.ModelAdmin):
    list_display=('name','created_at')    

class productAdmin(admin.ModelAdmin):
    list_display=('name','original_price','selling_price')    

admin.site.register(catagory,catagoryAdmin)
admin.site.register(product,productAdmin)

