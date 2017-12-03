from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.contrib import admin
from simple_history.models import HistoricalRecords

from django.db import models

# Create your models here.


class user_profile(models.Model):
    user = models.ForeignKey(User,related_name='user_profile')
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250 , blank = True)

    def __unicode__(self):
        return self.email

class user_notes(models.Model):
    user = models.ForeignKey(user_profile,related_name='user_profile_notes')
    note = models.CharField(max_length=250)
    primary_user = models.BooleanField(default=True)
    marked = models.BooleanField(default=False)
    original_note_id = models.CharField(max_length=250, blank = True, default = '')

    def __unicode__(self):
        return self.note