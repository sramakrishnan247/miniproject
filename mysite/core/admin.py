from django.contrib import admin
from .models import LandOwner,CarOwner, Security,Place

from django.contrib.auth.models import User

# Register your models here.
admin.site.register(LandOwner)
admin.site.register(CarOwner)
admin.site.register(Security)
admin.site.register(Place)
