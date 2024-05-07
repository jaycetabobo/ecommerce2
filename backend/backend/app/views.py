from django.shortcuts import render
from rest_framework.response import Response
from app.serializers import ProductSerializer, StoreSerializer, CategorySerializer, ProductSerializers
from app.models import Product, Store, Category
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView

class ProductListApiView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class ProductListApiViews(ListCreateAPIView):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()

    def perform_create(self, serializer):
        serializer.save()        

class ProductDetailApiView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class StoreListApiView(ListCreateAPIView):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class CategoryListApiView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class CategoryDetailApiView(RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

'''Gihimo ni nako para sa ProductSerializers para makita ang name jud
    dili ang id
'''
class ProductListByCategory(ListAPIView):
    serializer_class = ProductSerializers

    def get_queryset(self):
        category_name = self.kwargs['category']
        return Product.objects.filter(category__category=category_name)
