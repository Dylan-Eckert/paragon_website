# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re, bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def login(self, post):
        username = post['username'].lower()
        password = post['password']

        users = User.objects.filter(username=username)
        if len(users):
            user = users[0]
            if bcrypt.checkpw(password.encode(), user.password.encode()):
                return user

        return False

    def userIsValid(self, post):
        name = post['name']
        username = post['username'].lower()
        email = post['email'].lower()
        password = post['password']
        cpassword = post['cpassword']

        errors = []
        if len(name) < 2 :
             errors.append('Please enter a valid name')
        if len(username) < 6 or len(username) > 32:
             errors.append('Username has to be between 6-32 characters')
        # do all the email stuff like REGEX and shit IN THIS IF STATEMENT BELOW!!!!
        if len(email) < 6 or len(email) > 32:
             errors.append('Email has to be between 6-32 characters')
        elif not EMAIL_REGEX.match(email):
            errors.append('Please enter a valid email (something@something.something)')

        if len(password) < 8 or len(password) > 255:
             errors.append('Password has to be between 5-255 characters')
        elif password != cpassword:
            errors.append('Passwords do not match')

        if not errors:
            user_email = self.filter(email=email)
            if user_email:
                errors.append('Email already taken')
            user_username = self.filter(username=username)
            if user_username:
                errors.append('Username already taken')

        return {'status': len(errors) == 0, 'errors':errors}

    def newUser(self, post):
        name = post['name']
        username = post['username'].lower()
        email = post['email'].lower()
        password = post['password']

        hashp = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        return self.create(name=name, username=username, email = email, password = hashp)


class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=32)
    password = models.CharField(max_length=255)
    admin = models.IntegerField(default=0)
    master = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return "id: {}, name: {}, username: {}, email: {}, admin: {}, master: {}".format(self.id, self.name, self.username, self.email, self.admin, self.master)
