

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.utils import timezone
from django.contrib import messages
import json
from django.contrib.sessions.models import Session
from .models import Location,Event


class SearchView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loc = Location.objects.get(pk=30)
        events = Event.objects.get(pk=1)
        context['fromlist'] = loc.tileorder
        context['evs'] = loc.pk

    #
        return context
    # def get(self, request, *args, **kwargs):
    #     if 'fromlist' not in request.session:
    #         request.session['fromlist'] = []
    #     if 'tolist' not in request.session:
    #         request.session['tolist'] = []
    #     context = self.get_context_data()
    #     return render(request, self.template_name,context)
