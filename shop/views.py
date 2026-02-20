from django.shortcuts import render
from django.views.generic import ListView,DetailView

from .models import Product

class ProductList(ListView):
    model = Product
    queryset = Product.objects.filter(is_active=True)
    context_object_name = "products"
    template_name= 'shop/product_list.html'


class ProductDetail(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
    context_object_name = "product"  
    query_pk_and_slug = True  


class NewProduct(ListView):
    model = Product
    context_object_name = "products"
    template_name = 'shop/product_new.html'

    def get_queryset(self):
        return Product.objects.filter(is_active=True).order_by('-date_time_added')[:10]
