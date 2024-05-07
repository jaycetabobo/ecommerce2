from rest_framework import serializers
from app.models import Product, Store, Category
# from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer

class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'                


'''Diri dapit is mao ning code sa makita tanan fields pero sa category 
    og store kay dili niya makita, makita and id dili ang name jud sa 
    store og category
'''
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'productname', 'description', 'category', 'price', 'stock', 'store']


'''Mao dayon ni ngano akong gicreate ni na serializer kay makita niya
Like category: naay "Men, Women" itry gani ang link na 'products' og 
'productsss' sa urls
'''

class ProductSerializers(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    store = serializers.SerializerMethodField()
    
    def get_category(self, obj):
        return obj.category.category

    def get_store(self, obj):
        return obj.store.storename

    class Meta:
        model = Product
        fields = ['id', 'productname', 'description', 'category', 'price', 'stock', 'store']        





# class UserCreateSerializer(BaseUserCreateSerializer):
#     class Meta(BaseUserCreateSerializer.Meta):
#         fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']