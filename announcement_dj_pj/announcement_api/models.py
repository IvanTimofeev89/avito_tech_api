from django.core.validators import MinValueValidator
from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    price = models.PositiveIntegerField(
        verbose_name="Цена", validators=[MinValueValidator(1)]
    )
    description = models.TextField(max_length=1000, verbose_name="Описание")
    created_at = models.DateField(auto_now_add=True, blank=True, null=True)


class AdPicture(models.Model):
    link = models.ImageField(upload_to="img", blank=True, null=True)
    announcement = models.ForeignKey(
        Ad, on_delete=models.CASCADE, related_name="pictures", null=True, default=None
    )
