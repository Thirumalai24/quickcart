from django.contrib import admin
from .models import *

# inherit the model
class CategoryAdmin(admin.ModelAdmin): 
    list_display = ('name','image','description')
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','category', 'quantity')
    
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)