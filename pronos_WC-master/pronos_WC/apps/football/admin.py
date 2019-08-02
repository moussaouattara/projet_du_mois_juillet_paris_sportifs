# -*- coding: utf-8 -*-

from __future__ import (print_function, division, absolute_import, unicode_literals)

from django.contrib import admin
from imagekit.admin import AdminThumbnail
from pronos_WC.apps.football import models


class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'thumbnail', 'poule')

    thumbnail = AdminThumbnail(image_field='drapeau_admin_thumbnail')
    thumbnail.short_description = 'Drapeau'


class MatchAdmin(admin.ModelAdmin):
	list_display = ('vs', 'score','nb_pronostic', 'date', 'traite')
	ordering = ('date',)


class PronosticAdmin(admin.ModelAdmin):
    list_display = ('joueur','match','score')

class JoueurAdmin(admin.ModelAdmin):
    list_display = ('nom','points')



admin.site.register(models.Match, MatchAdmin)
admin.site.register(models.Equipe, EquipeAdmin)
admin.site.register(models.Pronostic, PronosticAdmin)
admin.site.register(models.Joueur, JoueurAdmin)
