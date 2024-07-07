from django.contrib import admin

# Register your models here.

# Do display and interact with the Models from django Admin Panel
from .models import *
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Tag)