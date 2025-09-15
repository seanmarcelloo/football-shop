from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('shorts', 'Shorts'),
        ('shoes', 'Football Shoes'),
        ('ball', 'Football'),
        ('equipment', 'Training Equipment'),
        ('accessories', 'Accessories'),
        ('merchandise', 'Merchandise'),
    ]
    
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='merchandise')
    is_featured = models.BooleanField(default=False)
    added_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.name