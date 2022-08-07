from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Item(models.Model):

    def __str__(self) -> str:
        return self.item_name

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default='https://assets.materialup.com/uploads/b03b23aa-aa69-4657-aa5e-fa5fef2c76e8/preview.png')
    
    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk":self.pk})