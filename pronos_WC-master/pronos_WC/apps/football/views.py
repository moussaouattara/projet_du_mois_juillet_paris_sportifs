from __future__ import (print_function, division, absolute_import, unicode_literals)

from django.views.generic import TemplateView, ListView, DetailView
from .models import Match, User, Pronostic, Joueur
from django.http import *
from django.shortcuts import redirect
from datetime import datetime
from django.utils.dateformat import DateFormat
import collections


class JoueurClassementView(ListView):
    template_name = 'joueur/classement.html'
    model = Joueur

    def get_queryset(self):
        return Joueur.objects.order_by('-points','user__last_name','user__first_name')

class MatchView(ListView):
    template_name = 'match/next.html'
    model = Match

    def get_context_data(self, **kwargs):
    	# Call the base implementation first to get a context.
    	context = super(MatchView, self).get_context_data(**kwargs)
	listMatch =  Match.objects.order_by('date').filter(date__gt=datetime.today())
	listMatchByDate={}
	for match in listMatch:
		if match.date not in listMatchByDate:
			listMatchByDate[match.date] = []

		listMatchByDate[match.date].append(match)

	listMatchByDate = collections.OrderedDict(sorted(listMatchByDate.items()))
    	context['match_list'] = listMatchByDate
    	return context

class MatchOldView(ListView):
    template_name = 'match/old.html'
    model = Match

    def get_context_data(self, **kwargs):
    	# Call the base implementation first to get a context.
    	context = super(MatchOldView, self).get_context_data(**kwargs)
	listMatch =  Match.objects.order_by('date').filter(traite=1)
	listMatchByDate={}
	for match in listMatch:
		if match.date not in listMatchByDate:
			listMatchByDate[match.date] = []

		listMatchByDate[match.date].append(match)

	listMatchByDate = collections.OrderedDict(sorted(listMatchByDate.items()))
    	context['match_list'] = listMatchByDate
    	return context


class MyPronosticsView(ListView):
    template_name = 'pronostics/list.html'
    model = Pronostic

    def get_queryset(self):
    	current_user = self.request.user
        return Pronostic.objects.order_by('-date').filter(joueur_id=current_user.id)


def add_pronostic(request):
    if request.method == 'POST': # If the form has been submitted...
    	current_user = request.user
    	dt = datetime.now()
    	df = DateFormat(dt)
        equipe1_score = request.POST['equipe1_score']
        equipe2_score = request.POST['equipe2_score']
        match_id = request.POST['match_id']
        pronostic = Pronostic(equipe1_result = equipe1_score, equipe2_result = equipe2_score, joueur_id = current_user.id, match_id = match_id, date = df.format('Y-m-d'))
        pronostic.save()
        # then return
        return redirect('match') # Redirect after POST
    
    return redirect('match')
