from rest_framework import status  # Add this import
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.http import require_POST
from rest_framework.response import Response
from .models import Product, Category, Cart, Review
from .serializers import ProductSerializer, CategorySerializer, CartSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from .serializers import CustomUserSerializer, ReviewSerializer
from rest_framework.views import APIView
from rest_framework import generics, permissions



@api_view(['POST'])
def add_product(request):
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Update status variable
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Update status variable

@api_view(['GET'])
def user_products(request, user_id):
    if request.method == 'GET':
        products = Product.objects.filter(user_id=user_id)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_all_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_product_by_id(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request):
    if request.method == 'POST':
        user = request.user
        product_id = request.data.get('product_id')
        try:
            product = Product.objects.get(id=product_id)
            cart_item, created = Cart.objects.get_or_create(user=user, product=product)
            if created:
                return Response({"message": "Product added to cart successfully"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "Product already exists in cart"}, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"error": "Product does not exist"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_cart(request):
    if request.method == 'GET':
        user = request.user
        cart_items = Cart.objects.filter(user=user)
        serializer = CartSerializer(cart_items, many=True)
        return Response(serializer.data)
    
#change username
@require_POST
def change_username(request):
    if request.user.is_authenticated:
        new_username = request.POST.get('new_username')
        if new_username:
            user = request.user
            user.username = new_username
            user.save()
            return JsonResponse({'message': 'Username changed successfully.'})
        else:
            return JsonResponse({'error': 'New username is required.'}, status=400)
    else:
        return JsonResponse({'error': 'User not authenticated.'}, status=401)
    
class ChangeUsernameView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_review(request):
    if request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"message": "Review added successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_reviews_for_product(request, product_id):
    try:
        reviews = Review.objects.filter(product_id=product_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    except Review.DoesNotExist:
        return Response({"error": "No reviews found for this product"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_all_reviews(request):
    try:
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    except Review.DoesNotExist:
        return Response({"error": "No reviews found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        if product.user != request.user:
            return Response({"error": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = ProductSerializer(instance=product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
    

    