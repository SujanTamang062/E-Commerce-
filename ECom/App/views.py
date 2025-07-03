from django.shortcuts import render
from django.contrib.auth.models import Group, User
from rest_framework import permissions,viewsets
from .models import Category,Product,CartItem,order,OrderItem,Payment
from .serializers import UserSerializer,GroupSerializer,CategorySerializer,ProductSerializer,CartItemSerializer,orderSerializer,OrderItemSerializer,PaymentSerializer

class DashboardView(viewsets.ModelViewSet):
    queryset = User
    serializer_class = UserSerializer
    
class RegisterView(viewsets.ModelViewSet):
    queryset = User
    serializer_class = UserSerializer
    
class LoginView(viewsets.ModelViewSet):
    queryset = User
    serializer_class = UserSerializer
    
    
class CategoryView(viewsets.ModelViewSet):
    queryset = Category
    serializer_class = CategorySerializer
    
class ProductView(viewsets.ModelViewSet):
    queryset = Product
    serializer_class = ProductSerializer
    
class CardItemView(viewsets.ModelViewSet):
    queryset = CartItem
    serializer_class = CartItemSerializer
    
class OrderView(viewsets.ModelViewSet):
    queryset = order
    serializer_class = orderSerializer
    
class OrderItemView(viewsets.ModelViewSet):
    queryset = OrderItem
    serializer_class = OrderItemSerializer
    
class PaymentView(viewsets.ModelViewSet):
    queryset = Payment
    serializer_class = PaymentSerializer
    
    


