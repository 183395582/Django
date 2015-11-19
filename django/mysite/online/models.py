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

class Teacher(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=False)
    gender = models.CharField(max_length=1, blank=True)
    address = models.CharField(max_length=200, blank=True)
    birthday = models.DateField(blank=True, null=True)
    seniority = models.IntegerField(blank=True, null=True)
    education = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=11, blank=True)
    email = models.CharField(max_length=50, blank=True)
    university = models.CharField(max_length=50, blank=True)
    entryDate = models.DateField(db_column='entryDate', blank=True, null=True) #Field name made lowercase.
    status = models.CharField(max_length=1, blank=False)
    mark = models.CharField(max_length=500, blank=True)
    class Meta:
        managed = False
        db_table = 'teacher'
