from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.BooleanField(blank=True, null=True)  # True for male, None for unknow
    age = models.PositiveIntegerField(blank=True, null=True)

    # follow subscribe
    follower = models.ManyToManyField(User, blank=True, related_name='prof_follower_set')
    followed = models.ManyToManyField(User, blank=True, related_name='prof_followed_set')

    def __str__(self):
        return f'{self.user.username}'
    

