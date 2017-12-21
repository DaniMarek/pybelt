from __future__ import unicode_literals
from apps.pybelt.models import User
from django.db import models


class User(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email_address = models.CharField(max_length=255)
  user_name = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __unicode__(self):
    return "id: " + str(self.id) + ", email: " + self.email


class UserManager(models.Manager):
  def login(self, postData):
    pass
    # insert code
    # return < return > 
class Compliment(models.Model):
  compliment = models.TextField()
  user = models.ForeignKey(User, related_name="comments")