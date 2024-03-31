from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name='category title')
    description = models.CharField(max_length=500, verbose_name='category description')

    def __str__(self):
        return f'title category: {self.title}'
