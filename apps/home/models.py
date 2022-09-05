# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from venv import create
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PlayerDetailsModel(models.Model):
    country = models.CharField(max_length = 100)
    competition = models.CharField(max_length = 100)
    club =  models.CharField(max_length = 100)
    player = models.CharField(max_length = 100)

    

