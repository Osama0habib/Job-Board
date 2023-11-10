from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey("City",related_name="user_city",on_delete=models.CASCADE,blank= True,null=True)
    phone = models.CharField(max_length=15)
    image = models.ImageField(upload_to='profile/')
    
    
    
    def __str__(self) -> str:
        return str(self.user) 

# create an empty profile when creating user
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
         
        
class City(models.Model):
    name = models.CharField(max_length=30) 
    
    def __str__(self) -> str:
        return str(self.name) 
    