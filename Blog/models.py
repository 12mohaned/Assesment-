from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Table Contain Users
class user(models.Model):
    username  = models.CharField(max_length = 50, primary_key = True)
    firstname = models.CharField(max_length = 50)
    lastname  = models.CharField(max_length = 50)
    Bio       = models.CharField(max_length = 100)

    def __str__(self):
        return self.username

#Table Contain Posts
class Post(models.Model):
    Title = models.CharField(max_length = 100)
    Content = models.TextField()
    User = models.ForeignKey(User, on_delete = models.CASCADE)

    class Meta:
        unique_together = ["Title","User"]
    def __str__(self):
        return self.Title

#Table Contain Comments on Posts
# Note !
# The Comment is automatically deleted if the user deleted his/her account or deleted the post
class Comment(models.Model):
    User_Comment = models.CharField(max_length = 50)
    Postuser = models.ForeignKey(User, on_delete = models.CASCADE)
    Content = models.TextField()
    Post = models.ForeignKey(Post, on_delete = models.CASCADE)

    def __str__(self):
        return "User: " + self.User_Comment + " Commented on Post of Title : "
