from django.db import models
from django.contrib.auth.models import User
from brand_model.models import BrandModel
from django.core.validators import MinValueValidator



# Create your models here.
class CarModel(models.Model):
    car_title = models.CharField(max_length=100)
    car_description = models.TextField()
    car_price = models.IntegerField(validators=[MinValueValidator(0)])
    car_model = models.ManyToManyField(BrandModel)
    car_quantity = models.IntegerField(validators=[MinValueValidator(0)],null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    car_image = models.ImageField(upload_to='uploads/')


    def __str__(self):
        return f"{self.car_title}"
