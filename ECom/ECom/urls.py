"""
URL configuration for ECom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from App.views import DashboardView,RegisterView,LoginView,CategoryView,ProductView,CardItemView,OrderView,PaymentView,OrderItemView

urlpatterns = [
    path('dashboard/', DashboardView.as_view({'get': 'list', 'post': 'create'})),
    path('register/', RegisterView.as_view({'post': 'create'})),
    path('login/', LoginView.as_view({'post': 'create'})),
    path('category/', CategoryView.as_view({'get': 'list', 'post': 'create'})),
    path('product/', ProductView.as_view({'get': 'list', 'post': 'create'})),
    path('cart/', CardItemView.as_view({'get': 'list', 'post': 'create'})),
    path('order/', OrderView.as_view({'get': 'list', 'post': 'create'})),
    path('order-item/', OrderItemView.as_view({'get': 'list', 'post': 'create'})),
    path('payment/', PaymentView.as_view({'get': 'list', 'post': 'create'})),
    
    
    path('admin/', admin.site.urls),
]
