# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from ..login_registration.models import User

# Create your views here.
# =========================================================
#                         VIEWS
# =========================================================
def index(request):

    return render(request, 'core/index.html')

# =========================================================
#                       HERO VIEWS
# =========================================================

def heros(request):
    if 'user_id' not in request.session:
        return redirect('/login_register/')

    user = User.objects.get(id=request.session['user_id'])
    heros = Hero.objects.all()

    data = {
    'user': user,
    'heros': heros
    }

    return render(request, 'core/heros.html', data)

def heroProf(request, hero_id):
    if 'user_id' not in request.session:
        return redirect('/login_register/')

    user = User.objects.get(id=request.session['user_id'])
    hero = Hero.objects.get(id=hero_id)
    roles = Role.objects.exclude(rec_heros=hero)

    data = {
    'hero': hero,
    'user': user,
    'roles': roles,
    }

    return render(request, 'core/heroprofile.html', data)

def updateHero(request, hero_id):
    if 'user_id' not in request.session:
        return redirect('/login_register/')
    user = User.objects.get(id=request.session['user_id'])
    if user.admin == 0:
        url = "/heroes/" + hero_id
        return redirect(url)

    hero = Hero.objects.get(id=hero_id)
    roles = Role.objects.exclude(rec_heros=hero)

    data = {
    'hero': hero,
    'roles': roles,
    }

    return render(request, 'core/admin_pages/updatehero.html', data)

def createHero(request):
    if 'user_id' not in request.session:
        return redirect('/login_register/')
    user = User.objects.get(id=request.session['user_id'])
    if user.master == 0:
        url = "/heros"
        return redirect(url)

    return render(request, 'core/master_pages/createhero.html')

# =========================================================
#                      ROLE VIEWS
# =========================================================

def roles(request):
    if 'user_id' not in request.session:
        return redirect('/login_register/')

    roles = Role.objects.all()
    user = User.objects.get(id=request.session['user_id'])

    data = {
    'roles': roles,
    'user': user,
    }

    return render(request, 'core/roles.html', data)

def roleProf(request, role_id):
    if 'user_id' not in request.session:
        return redirect('/login_register/')

    user = User.objects.get(id=request.session['user_id'])
    role = Role.objects.get(id=role_id)

    data = {
    'role': role,
    'user': user,
    }

    return render(request, 'core/roleprofile.html', data)

def updateRole(request, role_id):
    if 'user_id' not in request.session:
        return redirect('/login_register/')

    role = Role.objects.get(id=role_id)

    data = {
    'role': role,
    }

    return render(request, 'core/admin_pages/updaterole.html', data)

def createRole(request):
    if 'user_id' not in request.session:
        return redirect('/login_register/')

    return render(request, 'core/master_pages/createrole.html')
# =========================================================
#                        PROCESSES
# =========================================================

# =========================================================
#                     HERO PROCESSES
# =========================================================

def createNewHero(request):
    if 'user_id' not in request.session:
        return redirect('/login_register/')
    res = Hero.objects.heroIsValid(request.POST)

    if res['status']:
        hero = Hero.objects.newHero(request.POST)
    else:
        for error in res['errors']:
            messages.error(request, error)
        return redirect('/heroes/create')
    return redirect('/heros')

def updateThisHero(request, hero_id):
    if 'user_id' not in request.session:
        return redirect('/login_register/')

    Hero.objects.updateHero(hero_id, request.POST)

    url = "/heroes/" + hero_id
    return redirect(url)

def heroAddRole(request, hero_id, role_id):
    if 'user_id' not in request.session:
        return redirect('/login_register/')

    Hero.objects.heroAddRole(hero_id, role_id)
    url = "/heroes/update/" + hero_id
    return redirect(url)

def heroRemRole(request, hero_id, role_id):
    if 'user_id' not in request.session:
        return redirect('/login_register/')

    Hero.objects.heroRemRole(hero_id, role_id)
    url = "/heroes/update/" + hero_id
    return redirect(url)

# =========================================================
#                     ROLE PROCESSES
# =========================================================

def createNewRole(request):
    if 'user_id' not in request.session:
        return redirect('/login_register/')
    res = Role.objects.roleIsValid(request.POST)

    if res['status']:
        role = Role.objects.newRole(request.POST)
    else:
        for error in res['errors']:
            messages.error(request, error)
        return redirect('/roles/create')
    return redirect('/roles')

def updateThisRole(request, role_id):
    if 'user_id' not in request.session:
        return redirect('/login_register/')

    Role.objects.updateRole(role_id, request.POST)

    url = "/roles/" + role_id
    return redirect(url)

def roleAddHero(request, role_id, hero_id):
    pass

def roleAddHero(request, role_id, hero_id):
    pass
