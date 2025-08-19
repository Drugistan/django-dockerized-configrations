from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    discount = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_discounted_price(self):
        return self.price - (self.price * (self.discount / 100))