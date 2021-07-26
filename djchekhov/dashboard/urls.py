# -*- coding: utf-8 -*-

"""URLs for all views."""

from django.urls import path

from djchekhov.dashboard import views


urlpatterns = [
    path('', views.home, name='dashboard'),
]
