from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'get_products_count']
    prepopulated_fields = {
        'slug':['name',]
    }
    search_fields = ['name']
    ordering = ('name',)

    def get_products_count(self, obj):
        if hasattr(obj, 'product_set'):
             return obj.product_set.count()
        return 0 
    
    get_products_count.short_description = _("Product Count")

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price_main', 'price_with_discount', 'date_time_added']
    prepopulated_fields = {
        'slug':['title',]
    }
    search_fields = ['title']
    ordering = ('title',)