from django.db import models
from accounts.models import User

# Create your models here.

class Category_Job(models.Model):
    name = models.CharField(max_length=60)

class Recruitment_Post(models.Model):
    type = models.ForeignKey(Category_Job, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    title = models.CharField(max_length= 60)
    range = models.CharField(max_length= 40)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

'''
class Comments(models.Model):
    post = models.ForeignKey(Post,on_delete= models.CASCADE)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
'''
