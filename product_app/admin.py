from django.contrib import admin
from product_app.models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "price"]

admin.site.register(Product, ProductAdmin)
