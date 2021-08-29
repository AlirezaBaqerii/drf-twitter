from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# class TweetLike(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE )
#     tweet = models.ForeignKey('Tweet', on_delete=models.CASCADE)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return {self.user.username}


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # likes = models.ManyToManyField()
    content = models.TextField(max_length=280)
    timestamp = models.DateTimeField(default=timezone.now)
    is_drafted = models.BooleanField(default=False)
    is_tweeted = models.BooleanField(default=True)

    def __str__(self):
        return f"user: {self.user.username}-time:{self.timestamp}"
