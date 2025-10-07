import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
                             
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('shorts', 'Shorts'),
        ('shoes', 'Football Shoes'),
        ('ball', 'Football'),
        ('equipment', 'Training Equipment'),
        ('accessories', 'Accessories'),
        ('merchandise', 'Merchandise'),
    ]

    # uuid = models.UUIDField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='merchandise')
    is_featured = models.BooleanField(default=False)
    added_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
# class Employee(models.Model):
#     name = models.CharField(max_length=255)
#     age = models.IntegerField()
#     persona = models.TextField()

# class Book(models.Model):
#     id = models.UUIDField()
#     name  = models.CharField(max_length=255)

# class Author(models.Model):
#     bio = models.TextField()
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
#     books  = models.ManyToManyField(Book, on_delete = models.CASCADE, null=True)