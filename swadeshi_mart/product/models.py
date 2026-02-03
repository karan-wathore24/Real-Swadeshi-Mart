from django.db import models
from accounts.models import User

class Product(models.Model):
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'is_seller': True}
    )
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    image = models.ImageField(upload_to='products/') 

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
