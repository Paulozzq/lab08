from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True) 

    def __str__(self):
        return self.name


class Serie(models.Model):
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(10)] 
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='series'
    )

    def __str__(self):
        return f"{self.name} - {self.category.name}"
