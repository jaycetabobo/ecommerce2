
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from app.views import add_product, user_products, get_categories, get_all_products, get_product_by_id, add_to_cart, view_cart, change_username, add_review,get_reviews_for_product, get_all_reviews, update_product
from app import views

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    #for adding of products
    path('add_product/', add_product, name='add_product'),

    #products by user(seller)
    path('user_products/<int:user_id>/', user_products, name='user_products'),

    path('categories/', get_categories, name='categories'),

    #tanan products para makita ni customer
    path('products/', get_all_products, name='get_all_products'),

    #products by users
    path('products/<int:product_id>/', get_product_by_id, name='get_product_by_id'),

    path('cart/add/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart'),

    #accoun management
    path('api/change-username/', change_username, name='change_username'),
    path('change-username/', views.ChangeUsernameView.as_view(), name='change_username'),

    #review
    # path('review/', ReviewCreate.as_view(), name='review-create'),
    path('add_review/', add_review, name='add_review'),
    path('get_reviews/<int:product_id>/', get_reviews_for_product, name='get_reviews_for_product'),
    path('get_reviews/', get_all_reviews, name='get_all_reviews'),

    path('products/<int:product_id>/update/', update_product, name='update_product'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
