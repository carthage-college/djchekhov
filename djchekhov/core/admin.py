# -*- coding: utf-8 -*-

"""Admin classes for data models."""

from django.contrib import admin
from djchekhov.core.models import Accounts
from djchekhov.core.models import Compliance
from djchekhov.core.models import Emergency
from djchekhov.core.models import Housing
from djchekhov.core.models import Profile
from djchekhov.core.models import Registrar
from djchekhov.core.models import Services


class ProfileAdmin(admin.ModelAdmin):
    """User profile admin class."""

    list_display = ('profile_username', 'profile_firstname', 'profile_lastname')
    list_per_page = 500
    raw_id_fields = ('user',)

    date_hierarchy = 'created_at'
    #readonly_fields = ('user',)
    search_fields = (
        'user__username',
        'user__last_name',
        'user__first_name',
        'user__id',
    )

    def profile_username(self, instance):
        """Return user's username."""
        return instance.user.username
    profile_username.short_description = "username"

    def profile_firstname(self, instance):
        """Return user's given name."""
        return instance.user.first_name
    profile_firstname.short_description = "first name"

    def profile_lastname(self, instance):
        """Return user's sur name."""
        return instance.user.last_name
    profile_lastname.short_description = "last name"


admin.site.register(Accounts)
admin.site.register(Compliance)
admin.site.register(Emergency)
admin.site.register(Housing)
admin.site.register(Profile)
admin.site.register(Registrar)
admin.site.register(Services)
