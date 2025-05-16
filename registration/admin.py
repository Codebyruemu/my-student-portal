from django.contrib import admin
from .models import *

# Register your models here.


class courseAdmin(admin.ModelAdmin):
    list_display=['name','fee']
    list_filter=['name']
    
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','email','sex','address','phone','course','image','date']
    list_filter=['name','sex','phone','course','date']
class PaymentAdmin(admin.ModelAdmin):
    list_display=['student','amount','payment_date','payment_reference','payment_method']
    list_filter=['student','amount','payment_date']

admin.site.register(Course, courseAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Payment,PaymentAdmin)