from django.contrib import admin
from django.urls import path
from app.views import ProductListApiView, ProductListApiViews, StoreListApiView, ProductDetailApiView, CategoryListApiView, CategoryDetailApiView, ProductListByCategory

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', ProductListApiView.as_view(), name = 'product-list-view'),
    path('productsss/', ProductListApiViews.as_view(), name = 'product-list-view'),
    path('products/<int:pk>/', ProductDetailApiView.as_view(), name='product-detail-view'),
    path('category/', CategoryListApiView.as_view(), name = 'category-list-view'),
    path('category/<int:pk>/', CategoryDetailApiView.as_view(), name='product-detail-view'),
    path('<str:category>/products/', ProductListByCategory.as_view(), name='product-list-by-category'),
    path('stores/', StoreListApiView.as_view(), name = 'store-list-view'),
]
