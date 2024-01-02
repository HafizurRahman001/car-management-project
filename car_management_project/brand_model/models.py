from django.db import models
from django.utils.text import slugify

# Create your models here.
class BrandModel(models.Model):
    brand_name = models.CharField(max_length = 100, null=True,blank=True)
    slug = models.SlugField(max_length =100, unique = True, blank = True, null = True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.brand_name)
        super().save(*args, **kwargs)    


    def __str__(self):
        return f"{self.brand_name}"