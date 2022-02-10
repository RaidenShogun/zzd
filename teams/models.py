from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


# Create your models here.
""" Team
admin: can start a project
cadre: can manage member
member: can contribute to the project
"""
class Team(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    cadre = models.ManyToManyField(User, related_name='team_cadre_set', blank=True)
    member = models.ManyToManyField(User, related_name='team_member_set', blank=True)
    type = models.CharField(max_length=30) 
    # school 学校, team 团队, enterprise 企业  
    name = models.CharField(max_length=30)
    desc = models.TextField()
    createTime = models.DateTimeField(default=now, editable=False)
    canApply = models.BooleanField(default=True)
    # create admin feedback
    invited = models.ManyToManyField(User, related_name='team_invited_set', blank=True)
    accepted = models.ManyToManyField(User, related_name='team_accept_set', blank=True)
    rejected = models.ManyToManyField(User, related_name='team_reject_set', blank=True)
