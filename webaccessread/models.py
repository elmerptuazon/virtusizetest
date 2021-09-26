from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class WebAccessRead(models.Model):
    link = models.CharField(default="",max_length=300)
    word = models.CharField(default="",max_length=64)
    count = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(999)])
    class Meta:
        db_table='webaccessread_webaccessread'
    