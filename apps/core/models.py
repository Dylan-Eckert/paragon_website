# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login_registration.models import *

# Create your models here.
class RoleManager(models.Manager):
    def roleIsValid(self, post):
        name = post['name']
        desc = post['desc']
        tips = post['tips']

        errors = []
        if len(name) < 2 :
             errors.append('Please enter a valid name')
        if len(desc) < 2 :
             errors.append('Please enter a valid desc')
        if len(tips) < 2 :
             errors.append('Please enter a valid tips')

        return {'status': len(errors) == 0, 'errors':errors}

    def newRole(self, post):
        name = post['name']
        desc = post['desc']
        tips = post['tips']

        new_role = self.create(name=name, desc=desc, tips=tips)

        return new_role

    def updateRole(self, roleid, post):
        role = Role.objects.get(id=roleid)

        role.name = post['name']
        role.desc = post['desc']
        role.tips = post['tips']

        role.save()

        return role

    def addRecHero(self, roleid, heroid):
        pass

    def remRecHero(self, roleid, heroid):
        pass

class HeroManager(models.Manager):
    def heroIsValid(self, post):
        name = post['name']
        desc = post['desc']
        tips = post['tips']
        ability1 = post['ability1']
        ability2 = post['ability2']
        ability3 = post['ability3']
        ability4 = post['ability4']
        abdesc1 = post['abdesc1']
        abdesc2 = post['abdesc2']
        abdesc3 = post['abdesc3']
        abdesc4 = post['abdesc4']

        errors = []
        if len(name) < 2 :
             errors.append('Please enter a valid name')
        if len(desc) < 2 :
             errors.append('Please enter a valid desc')
        if len(tips) < 2 :
             errors.append('Please enter a valid tips')
        if len(ability1) < 2 :
             errors.append('Please enter a valid ability')
        if len(ability2) < 2 :
             errors.append('Please enter a valid ability')
        if len(ability3) < 2 :
             errors.append('Please enter a valid ability')
        if len(ability4) < 2 :
             errors.append('Please enter a valid ability')
        if len(abdesc1) < 2 :
             errors.append('Please enter a valid ability description')
        if len(abdesc2) < 2 :
             errors.append('Please enter a valid ability description')
        if len(abdesc3) < 2 :
             errors.append('Please enter a valid ability description')
        if len(abdesc4) < 2 :
             errors.append('Please enter a valid ability description')

        return {'status': len(errors) == 0, 'errors':errors}

    def newHero(self, post):
        name = post['name']
        desc = post['desc']
        tips = post['tips']
        ability1 = post['ability1']
        ability2 = post['ability2']
        ability3 = post['ability3']
        ability4 = post['ability4']
        abdesc1 = post['abdesc1']
        abdesc2 = post['abdesc2']
        abdesc3 = post['abdesc3']
        abdesc4 = post['abdesc4']

        new_hero = self.create(name=name, desc=desc, tips=tips, ability1=ability1, ability2=ability2, ability3=ability3, ability4=ability4, abdesc1=abdesc1, abdesc2=abdesc2, abdesc3=abdesc3, abdesc4=abdesc4)

        return new_hero

    def updateHero(self, heroid, post):
        hero = Hero.objects.get(id=heroid)

        hero.name = post['name']
        hero.desc = post['desc']
        hero.tips = post['tips']
        hero.ability1 = post['ability1']
        hero.ability2 = post['ability2']
        hero.ability3 = post['ability3']
        hero.ability4 = post['ability4']
        hero.abdesc1 = post['abdesc1']
        hero.abdesc2 = post['abdesc2']
        hero.abdesc3 = post['abdesc3']
        hero.abdesc4 = post['abdesc4']

        hero.save()

        return hero

    def heroAddRole(self, heroid, roleid):
        if Hero.objects.filter(id=heroid).exists():
            hero = Hero.objects.get(id=heroid)
            role = Role.objects.get(id=roleid)
            hero.roles.add(role)

    def heroRemRole(self, heroid, roleid):
        if Hero.objects.filter(id=heroid).exists():
            hero = Hero.objects.get(id=heroid)
            role = Role.objects.get(id=roleid)
            hero.roles.remove(role)


class Role(models.Model):
    name = models.CharField(max_length=32)
    desc = models.TextField()
    tips = models.TextField()
    users_maining = models.ManyToManyField(User, related_name="main_roles", default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = RoleManager()

    def __str__(self):
        return "id: {}, name: {}".format(self.id, self.name)

class Hero(models.Model):
    name = models.CharField(max_length=32)
    ability1 = models.CharField(max_length=32)
    abdesc1 = models.TextField()
    ability2 = models.CharField(max_length=32)
    abdesc2 = models.TextField()
    ability3 = models.CharField(max_length=32)
    abdesc3 = models.TextField()
    ability4 = models.CharField(max_length=32)
    abdesc4 = models.TextField()
    desc = models.TextField()
    tips = models.TextField()
    users_maining = models.ManyToManyField(User, related_name="main_heros", default=None)
    roles = models.ManyToManyField(Role, related_name="rec_heros", default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = HeroManager()

    def __str__(self):
        return "id: {}, name: {}".format(self.id, self.name)
