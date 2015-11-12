from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __unicode__(self):
        return self.username

class Menu(models.Model):
    menu_name = models.CharField(max_length=20)
    menu_url = models.CharField(max_length=100)
    parent_id = models.IntegerField()
    menu_order = models.IntegerField()
    menu_icon = models.CharField(max_length=20)
    menu_type = models.IntegerField()
    def __unicode__(self):
        return self.menu_name