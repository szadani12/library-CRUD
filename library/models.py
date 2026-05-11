from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=70)
    author = models.CharField(max_length=70)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='book_category')
    year = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.title
