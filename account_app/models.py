from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    father_name = models.CharField(max_length=25)
    melli_code = models.CharField(max_length=10)
    image = models.ImageField(upload_to="profiles/images")
    
    def __str__(self):
        return f"{self.user.username} - {self.melli_code}" 