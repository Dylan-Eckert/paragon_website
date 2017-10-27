from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^heroes$', views.heros),
    url(r'^heroes/create$', views.createHero),
    url(r'^heroes/create/new$', views.createNewHero),
    url(r'^heroes/update/(?P<hero_id>\d+)$', views.updateHero),
    url(r'^heroes/update/(?P<hero_id>\d+)/updating$', views.updateThisHero),
    url(r'^heroes/(?P<hero_id>\d+)$', views.heroProf),
    url(r'^heroes/(?P<hero_id>\d+)/role/(?P<role_id>\d+)/add$', views.heroAddRole),
    url(r'^heroes/(?P<hero_id>\d+)/role/(?P<role_id>\d+)/rem$', views.heroRemRole),
    url(r'^roles$', views.roles),
    url(r'^roles/create$', views.createRole),
    url(r'^roles/create/new$', views.createNewRole),
    url(r'^roles/update/(?P<role_id>\d+)$', views.updateRole),
    url(r'^roles/update/(?P<role_id>\d+)/updating$', views.updateThisRole),
    url(r'^roles/(?P<role_id>\d+)$', views.roleProf),
]
