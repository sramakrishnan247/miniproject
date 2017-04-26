from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class LandOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lat = models.FloatField( blank=True, null=True)
    lon = models.FloatField( blank=True, null=True)
    pincode = models.IntegerField(blank=False)
    email = models.EmailField(max_length=50,blank=True)
    placename = models.CharField(max_length=40, blank=True)
    earnings = models.FloatField(blank=True, null=True)
    def __str__(self):
    	return str(self.user)

class CarOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50,blank=True)
    name = models.CharField(max_length=70, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    def __str__(self):
    	return str(self.user)

class Security(models.Model):   
    user = models.OneToOneField(LandOwner, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user)


class Place(models.Model):
    placename = models.OneToOneField(LandOwner,on_delete=models.CASCADE,)
    vacancy = models.IntegerField()
    def __str__(self):
        return str(self.placename)



# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()
