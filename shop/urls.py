from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    path('products/', views.ProductList.as_view(), name='product_list')
]
