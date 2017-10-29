# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nik = models.CharField(max_length=20, null=False)
    nama = models.CharField(max_length=35, null=True)
    email = models.EmailField(null=True)
    img = models.ImageField(upload_to='member/')

    class Meta:
        db_table = 'member'

    def __str__(self):
        return self.nama
