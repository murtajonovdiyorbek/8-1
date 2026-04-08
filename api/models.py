from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cars')
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    mileage = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='cars/', blank=True, null=True)



    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"