from django.db import models



class Article(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{ self.name } ({ self.unit_price })"
    
    