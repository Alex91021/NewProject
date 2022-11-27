from django.views.generic import ListView, DetailView
from .models import Product, Category


class ProductsList(ListView):
    model = Product
    ordering = 'name'
    template_name = 'products.html'
    context_object_name = 'products'


class CategorysList(ListView):
    model = Category
    ordering = 'name'
    template_name = 'categorys.html'
    context_object_name = 'categorys'


class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'
