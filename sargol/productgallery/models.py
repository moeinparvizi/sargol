from django.db import models
from web.models import products
# Create your models here.
class gallery(models.Model):

    img = models.ImageField(upload_to='product_gallery')
    productt = models.ForeignKey(products, on_delete=models.CASCADE)