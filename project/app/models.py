from django.db import models

# Create your models here.
class UserProfile(models.Model):
    username = models.CharField('username',max_length=100)
    email = models.EmailField('email',max_length=100)
    phone= models.IntegerField('phone')

    def __str__(self):
        return f"Name: {self.username}, Email: {self.email}, Phone: {self.phone}"