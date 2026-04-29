from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=70)
    author = models.CharField(max_length=70)
    category = models.CharField(max_length=70)
    year = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.title
