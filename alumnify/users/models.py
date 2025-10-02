from django.db import models

# Create your models here.
class User(models.Model):
    user_id=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    created_at=models.CharField(max_length=50)

    def __str__(self):
        return self.user_id + '' + self.username
