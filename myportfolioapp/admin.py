from django.contrib import admin
from .models import *

# Register your models here that is the only way you can see it in admin dashboard.
# username:refo
# password:hppavilion
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['firstName', 'lastName','email','phone','image','address','description','date']
    
    list_filter = ['firstName','lastName','address','date']
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','description','price','image','date')
    list_filter = ('name', 'price','date')
    
    
admin.site.register(profile,ProfileAdmin)
admin.site.register(Product,ProductAdmin)
