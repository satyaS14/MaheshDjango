# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import datetime

# Create your models here.
class dumpYard(models.Model):

    name = models.CharField(max_length=50)
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)

    # -1 - bad, 0 - ok, 1 - good
    severity = models.IntegerField(default=0)

    def __str__(self):
        return self.name + " " + str(self.lat) + " " + str(self.lng)


class userType(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    isAgent = models.BooleanField(default=False)
    isGovt = models.BooleanField(default=False)
    isAdmin = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.username)

class Agent(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    agentRFID = models.IntegerField(default=-1)
    agentScore = models.IntegerField(default=0)

    def __str__(self):
        return str(self.agentRFID)


class actions(models.Model):

    yard = models.OneToOneField(dumpYard, on_delete=models.CASCADE)
    agent = models.OneToOneField(Agent, on_delete=models.CASCADE)