from django.db import models
from django import forms
from car_model.models import CarModel
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comments by {self.name}"
    



# models.py
class Purchase(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    product = models.ForeignKey(CarModel, on_delete=models.CASCADE, null=True,blank=True)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.car_title}"
