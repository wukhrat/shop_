from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    description = models.CharField(max_length=500, verbose_name='category description')
    title = models.CharField(max_length=100, verbose_name='category title')
    amount = models.IntegerField(verbose_name='product amount')
    price = models.FloatField(verbose_name='product price')
    images = models.CharField(verbose_name='product image')
    active = models.BooleanField(verbose_name='active')

    def __str__(self):
        return f'title: {self.title}  price: {self.price}   amount: {self.amount}'
