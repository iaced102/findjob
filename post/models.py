from django.db import models
from accounts.models import User

# Create your models here.

class Category_Job(models.Model):
    name = models.CharField(max_length= 50)
    
    def __str__(self):
        return self.name

class Recruitment_Post(models.Model):
    type = models.ForeignKey(Category_Job, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    title = models.CharField(max_length= 60)
    range = models.CharField(max_length= 40)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)

    

    def __str__(self):
        return self.title
    

class Recruitment_Comments(models.Model):
    post = models.ForeignKey(Recruitment_Post,on_delete= models.CASCADE)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)

#models review post


class Review_Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    rate = models.IntegerField()
    count_rate = models.IntegerField()

class Review_Comments(models.Model):
    post = models.ForeignKey(Review_Post, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    rate = models.IntegerField()

class User_Rate(models.Model):
    post = models.ForeignKey(Review_Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

