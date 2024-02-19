from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


# Create your models here.
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) #it could be left null as well as being sent as a form null for the 2nd parameter.
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True) # every time the saved method is called it takes a timestamp and save it here automatically.
    created = models.DateTimeField(auto_now_add=True) # It only takes a timestamp when the instance is created (not every time is saved)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self) -> str:
        return self.name
    

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE) #One to many relationship, 1 room N messages.
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True) # every time the saved method is called it takes a timestamp and save it here automatically.
    created = models.DateTimeField(auto_now_add=True) # It only takes a timestamp when the instance is created (not every time is saved)
    
    class Meta:
        ordering = ['-updated', '-created']
    
    def __str__(self) -> str:
        return self.body[0:50] #trimming the message up to 50 characters.

