from django.db import models
from django.urls import reverse

# Create your models here
class Info(models.Model):
    address =models.CharField( max_length=50)
    phone =models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    
    

    class Meta:
        verbose_name = ("Info")
        verbose_name_plural = ("Infos")

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("Info_detail", kwargs={"pk": self.pk})



