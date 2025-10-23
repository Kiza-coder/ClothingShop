from django.db import models
from django.conf import settings
from decimal import Decimal
from articles.models import Article
import uuid


class Order(models.Model):
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE, 
    )
    
    status= models.CharField(
        max_length=20,
        choices = [
            ('pending','Pending'),
            ('processing','Processing'),
            ('completed','Completed'),
            ('cancelled','Cancelled'),
        ],
        default = 'pending'
    )
    
    reference = models.CharField(max_length=50,unique=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))
    
    def __str__(self):
        return f"Order { self.reference } by { self.user.username }"
    
    def save(self, *args, **kwargs):
        if not self.reference:
            self.reference = f"CMD-{ uuid.uuid4().hex[:8].upper() }"
        super().save(*args, **kwargs)
        
    
    
class OrderItem(models.Model):
    
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
    )
    
    article = models.ForeignKey(
        Article,
        on_delete=models.PROTECT,
    )
    
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=2,decimal_places=2)
    
    def __str__(self):
        return f"{ self.quantity} x { self.article.name }  in  order :{ self.order.reference }"
    
    @property
    def total_item_price(self):
        return  self.quantity  *  self.unit_price 
    
    class Meta:
        unique_together = ('order', 'article')
    