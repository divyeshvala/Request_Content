from django.db import models
from django.contrib.auth.models import User
from content.models import Topic, Creator

class TopicsFollowing(models.Model):
    username = models.CharField(max_length=100) 
    topics_following = models.ForeignKey(Topic, on_delete=models.CASCADE)   # many to one field

class CreatorsFollowing(models.Model):
    username = models.CharField(max_length=100) 
    creator_following = models.ForeignKey(Creator, on_delete=models.CASCADE)
	