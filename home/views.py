from django.shortcuts import render
from django.views.generic import TemplateView


class ProductHome(TemplateView):
    template_name ='home/home.html'


