from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify  # Converts text into URL-friendly slug

#Category
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(blank=True, unique=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:     # Auto-generate slug if not manually given
            self.slug = slugify(self.name)
        super().save(*args,**kwargs)   # Call original save method
        
    def __str__(self):
        return self.name  # Display category name in admin panel
    


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True,blank=True) 
    description = models.TextField(blank=True)    # Product description (optional)
    price = models.DecimalField(max_digits=10,decimal_places=2)   
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/',blank=True,null=True)    # Product image
    is_avilable = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:    # Auto-create slug from name
            self.slug = slugify(self.name)
        super().save(*args,**kwargs)
        
    def __str__(self):
        return self.name
    
    
class CartItem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)
    
    def total_price(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return f"{self.quantity} * {self.product.name}"
    
    

class order(models.Model):
    STATUS_CHOICES = (
        ('pending','Pending'),
        ('processing','Processing'),
        ('completed','Completed'),
        ('cancelled','Cancelled'),
        
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='pending')
    total_amount = models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return f"order #{self.id} by {self.user.username}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(order,related_name='items',on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def subtotal(self):
        return self.quantity * self.price
    
    def __str__(self):
        return f"{self.product.name} ({self.quantity})"
    

class Payment(models.Model):
    order = models.OneToOneField(order, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50) #khalti esewa
    payment_status = models.CharField(max_length=50, default="pending")
    transaction_id = models.CharField(max_length=100,blank=True,null=True)
    paid_at = models.DateTimeField(blank=True,null=True)
    
    def __str__(self):
        return f"payment for order #{self.order.id}"