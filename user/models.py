from django.db import models
from django.contrib.auth.admin import UserAdmin

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length= 50)


class CustomUser(UserAdmin):
    
    fieldsets = (
            (None, {"fields": ("username", "password")}),
            (("Personal info"), {"fields": ("first_name", "last_name", "email")}),
            
            (("Important dates"), {"fields": ("last_login", "date_joined")}),
        )
       