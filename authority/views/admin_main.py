from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import F
from datetime import timedelta
from datetime import datetime

# generic views
from django.views.generic import TemplateView

# Create your views here.
class AdminHomeView(TemplateView):
    template_name = 'authority/admin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'title' 
        return context
    