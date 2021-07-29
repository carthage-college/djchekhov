# -*- coding: utf-8 -*-

"""URLs for all views."""

import os

from django.conf import settings
from django.contrib.auth.models import User
from django.core.cache import cache
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from djauth.decorators import portal_auth_required


@portal_auth_required(
    session_var='DJCHEKHOV_AUTH',
    redirect_url=reverse_lazy('access_denied'),
    group=settings.MANAGERS_GROUP,
)
def home(request):
    """Dashboard home for administrators."""
    students =  User.objects.exclude(profile__program__isnull=True).exclude(profile__program='')
    return render(request, 'dashboard/home.html', {'students': students})
