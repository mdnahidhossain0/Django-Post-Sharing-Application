from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):
    content = models.TextField()
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweets')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profiles/', default='profiles/default.png')

    def __str__(self):
        return self.user.username
