from django.shortcuts import render

# Create your views here.

from .models import Category
from rest_framework import viewsets
from .serializer import CategorySerializer

# Após o comentario "# Create your views here." e crie as views "Category".

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer