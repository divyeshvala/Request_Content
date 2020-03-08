from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Idea(models.Model):
    idea_title = models.CharField(max_length=100)
    idea_description = models.TextField()
    likes = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)   # many to one field

class Topic(models.Model):
    followers_count = models.IntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField()

# one topic can have many creators and one creator can create many topics.

class Creator(models.Model):
    followers_count = models.IntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.IntegerField()
    topics = models.ManyToManyField(Topic)



    
    
