from django.db import models

# Create your models here.


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='pizzas/', blank=True, null=True)
    def __str__(self):
        return self.name