from django.db import models
from django.contrib.auth.models import AbstractUser

class todo_User(AbstractUser):
    userId = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=10,null=True,blank=True,unique=True)
    email=models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    
    def __str__(self):
        return f"{self.userId} - {self.username} - {self.email}- {self.phone_number}"

class Task(models.Model):

    user = models.ForeignKey(todo_User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
