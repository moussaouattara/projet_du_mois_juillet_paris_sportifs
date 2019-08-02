# -*- coding: utf-8 -*-

from __future__ import (print_function, division, absolute_import, unicode_literals)

from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.models import ImageSpecField
from imagekit.processors import Adjust, ResizeToFill, SmartCrop
from django.contrib.auth.models import User, AbstractUser
from django import forms
from django.db.models.signals import post_save
from django.dispatch import receiver


class Joueur(models.Model):
	user = models.OneToOneField(User)
	mobile = models.CharField(max_length=16, blank=True, null=True)
	points = models.PositiveIntegerField(blank=True, null=True)

	def __str__(self):
		return self.user.last_name+' '+self.user.first_name

	def nom(self):
	    return ("%s  %s" % (self.user.last_name, self.user.first_name))
	nom.short_description = 'Joueur'

@receiver(post_save, sender=User)
def create_joueur(sender, instance, signal, created, **kwargs):
    if created:
        instance.joueur = Joueur()
	instance.joueur.points = 0
        instance.joueur.save()
        instance.save()


class Equipe(models.Model):
	POULE_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
        ('G', 'G'),
        ('H', 'H'),
    )
	nom = models.CharField(max_length=255)
	poule = models.CharField(max_length=1, choices=POULE_CHOICES, default='A')
	drapeau = models.ImageField(upload_to='drapeau', null=True, blank=True, verbose_name=u'Drapeau')
	drapeau_thumbnail = ImageSpecField(source='drapeau',
	processors=[ResizeToFill(75, 50)],
	format='JPEG',
	options={'quality': 60})
	drapeau_admin_thumbnail = ImageSpecField(source='drapeau',
	processors=[ResizeToFill(50, 25)],
	format='JPEG',
	options={'quality': 60})

	def __str__(self):
		return self.nom

	def __unicode__(self):
   		return u'%s' % (self.nom)

	class Meta:
		ordering = ['poule','nom']


class Match(models.Model):
	TYPE_CHOICES = (
        ('Match de poule', 'Match de poule'),
        ('16eme de finale', '16eme de finale'),
        ('Quart de finale', 'Quart de finale'),
        ('Demi finale', 'Demi finale'),
        ('Finale', 'Finale'),
    )
	niveau = models.CharField(max_length=20, choices=TYPE_CHOICES, default='Match de poule')
	equipe1 = models.ForeignKey(Equipe, related_name='equipe1_content_type')
	equipe2 = models.ForeignKey(Equipe, related_name='equipe2_content_type')
	equipe1_result = models.PositiveIntegerField(blank=True, null=True)
	equipe2_result = models.PositiveIntegerField(blank=True, null=True)
	traite = models.BooleanField(default=False)
	date = models.DateField(blank=True, null=True)

	def __str__(self):
		return self.equipe1.nom+' - '+self.equipe2.nom

	def __unicode__(self):
   		return u'%s - %s' % (self.equipe1.nom,self.equipe2.nom)

	def save(self, *args, **kwargs):
		if self.equipe1_result is not None and self.equipe2_result is not None and self.traite == False:
			pronostics = Pronostic.objects.filter(match_id=self.id)
			for pronostic in pronostics:
				points_sup = 0
				if (self.equipe1_result > self.equipe2_result and pronostic.equipe1_result > pronostic.equipe2_result) or (self.equipe1_result < self.equipe2_result and pronostic.equipe1_result < pronostic.equipe2_result) or (self.equipe1_result == self.equipe2_result and pronostic.equipe1_result == pronostic.equipe2_result):
					points_sup = points_sup + 4
				if self.niveau != "Match de poule":
					if self.equipe1_result == pronostic.equipe1_result and self.equipe2_result == pronostic.equipe2_result:
						points_sup = points_sup + 2
					elif (self.equipe1_result - self.equipe2_result) == (pronostic.equipe1_result - pronostic.equipe2_result):
						points_sup = points_sup + 1

				if points_sup != 0 :
					user = User.objects.filter(id=pronostic.joueur_id)[0]
					joueur = Joueur.objects.filter(user_id=user.id)[0]
					joueur.points = joueur.points + points_sup
					joueur.save()
			self.traite = True
		super(Match, self).save(*args, **kwargs)

	def vs(self):
	    return ("%s - %s" % (self.equipe1.nom, self.equipe2.nom))
	vs.short_description = 'Confrontation'

	def nb_pronostic(self):
		return "%d / %d" % (Pronostic.objects.filter(match_id=self.id).count(), User.objects.count()) 
	nb_pronostic.short_description = 'Nombre de pronostics'

	@property
	def score(self):
	    return ("%s - %s" % (self.equipe1_result, self.equipe2_result))

	@property
	def getPronosticUserIds(self):
		pronosticUserIds = Pronostic.objects.filter(match_id=self.id).values_list('joueur_id', flat=True)
		return pronosticUserIds


class Pronostic(models.Model):
	joueur = models.ForeignKey(User)
	match = models.ForeignKey(Match)
	equipe1_result = models.PositiveIntegerField(blank=True, null=True)
	equipe2_result = models.PositiveIntegerField(blank=True, null=True)
	date = models.DateField(blank=True, null=True)

	@property
	def score(self):
	    return ("%s - %s" % (self.equipe1_result, self.equipe2_result))

	class Meta:
		unique_together = ('joueur', 'match',)
