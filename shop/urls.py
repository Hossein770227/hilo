from django.urls import path

from . import views

app_name = 'shop'


urlpatterns = [
    path('products/', views.ProductList.as_view(), name='product_list'),
    path('product/<slug:slug>/', views.ProductDetail.as_view(), name='product_detail'),
    path('products/new/', views.NewProduct.as_view(), name ='new_product'),
]
