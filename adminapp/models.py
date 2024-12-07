from django.db import models

# Create your models here.
class Recipe_suggestor(models.Model):
    objects = None
    ingredients = models.CharField(max_length=200)
    recipe = models.CharField(max_length=200)
    def _str_(self):
        return self.ingredients


from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField()

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order for {self.product.name} by {self.user.username}"
