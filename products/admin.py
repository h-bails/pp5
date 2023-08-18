from django.contrib import admin
from .models import Product, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'measurements',
        'condition',
        'price',
        'sku',
        'category',
        'image_1',
        'image_1_url',
    )

    ordering = ('date_added',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
    )
    
    ordering = ('name',)



admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)