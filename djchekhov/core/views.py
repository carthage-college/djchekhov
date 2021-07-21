# -*- coding: utf-8 -*-

"""All views."""

import datetime
import json
import requests

from django.conf import settings
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.decorators.csrf import csrf_exempt
from djauth.decorators import portal_auth_required
from djtools.utils.convert import str_to_class

TITLES = {
    'accounts': "Student Accounts and Financial Aid",
    'compliance': "Compliance Documents",
    'emergency': "Emergency Contact and International Student Insurance",
    'housing': "Campus Housing and Meal Plan",
    'registrar': "Email, Schoology, OneLogin, and Registrar",
    'services': "Student ID and Parking Permit",
}

@portal_auth_required(
    session_var='DJINDAHAUS_AUTH',
    redirect_url=reverse_lazy('access_denied'),
)
def home(request):
    """Display the check-in main view."""
    return render(request, 'home.html', {})


@portal_auth_required(
    session_var='DJINDAHAUS_AUTH',
    redirect_url=reverse_lazy('access_denied'),
)
def forms(request, slug):
    """Check-in view for all forms."""
    form_title = TITLES[slug]
    slug = slug.capitalize()
    form_class = str_to_class(
        'djchekhov.core.forms', '{0}Form'.format(slug),
    )
    if request.method == 'POST':
        form = form_class(
            request.POST,
            use_required_attribute=settings.REQUIRED_ATTRIBUTE,
        )
        if form.is_valid():
            reg = form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Success.",
                extra_tags='alert-success',
            )
            return HttpResponseRedirect(reverse_lazy('home'))
    else:
        form = form_class(
            use_required_attribute=settings.REQUIRED_ATTRIBUTE,
        )

    context = {'form': form, 'form_title': form_title}
    return render(request, 'forms.html', context)


@csrf_exempt
@portal_auth_required(
    session_var='DJINDAHAUS_AUTH',
    redirect_url=reverse_lazy('access_denied'),
    group='carthageStaffStatus',
)
def clear_cache(request, ctype='blurb'):
    """Clear the cache for API content."""
    if request.is_ajax() and request.method == 'POST':
        cid = request.POST.get('cid')
        key = 'livewhale_{0}_{1}'.format(ctype, cid)
        cache.delete(key)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        earl = '{0}/live/{1}/{2}@JSON?cache={3}'.format(
            settings.LIVEWHALE_API_URL, ctype, cid, timestamp,
        )
        try:
            response = requests.get(earl, headers={'Cache-Control': 'no-cache'})
            text = json.loads(response.text)
            cache.set(key, text)
            body = mark_safe(text['body'])
        except Exception:
            body = ''
    else:
        body = "Requires AJAX POST"

    return HttpResponse(body, content_type='text/plain; charset=utf-8')
