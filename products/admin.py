from django.contrib import admin
# need to now import and register the product & category model 
from .models import Product, Category

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
