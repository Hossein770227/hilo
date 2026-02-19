from django.shortcuts import render
from django.views.generic import ListView

from .models import Product

class ProductList(ListView):
    model = Product
    queryset = Product.objects.filter(is_active=True)
    context_object_name = "products"
    template_name= 'shop/product_list.html'
