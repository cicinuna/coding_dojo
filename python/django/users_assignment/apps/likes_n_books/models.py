from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __repr__(self):
        return "Name: {} {}.".format(self.first_name, self.last_name)

class Book(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now= True)
    uploader = models.ForeignKey(User, related_name = "uploaded_books")
    liked_users = models.ManyToManyField(User, related_name = "liked_books")

    def __repr__(self):
        return "Name: {}".format(self.name)