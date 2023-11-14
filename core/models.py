from django.db import models
import uuid
# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category

class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE ,verbose_name='category')
    item_name = models.CharField(max_length=255, verbose_name='item name')
    price = models.IntegerField(verbose_name='item price')
    quantity = models.IntegerField(verbose_name='quantity')
    expiration_date = models.CharField(max_length=255, verbose_name='expiration date')
    CARD_CHOICES = (
    ("UZCARD", "uzcard"),
    ("HUMO", "humo"),
    )
    paymet = models.CharField(max_length=9,
                  choices=CARD_CHOICES,
                  default="UZCARD")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique = True)

    def __str__(self):
        return self.item_name    