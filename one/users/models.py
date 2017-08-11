# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
"""
    this is user base information
"""



class User(models.Model):
    name = models.CharField(max_length = 30, unique=True,  null = False)
    pwd = models.CharField(max_length = 30,  null = False)
    age = models.IntegerField(null = True, default = 20)
    occupation = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 50,  null = False)
    level = models.IntegerField(null = True, default = 0)

    def __unicode__(self):
        return self.name
        pass

    def query_all(self):
        return User.objects.all().values('name', 'pwd')
        pass

    def add_user(self, useinfo):
        self.name = useinfo.get('name')
        self.pwd = useinfo.get('pwd')
        self.age = useinfo.get('age')
        self.occupation = useinfo.get('occupation')
        self.email = useinfo.get('email')
        self.save()
        pass

    def query_id(self, name):
        return User.objects.get(name = name)
        pass
