# -*- coding: utf-8 -*-

from django import forms

from djchekhov.core.models import Accounts
from djchekhov.core.models import Compliance
from djchekhov.core.models import Emergency
from djchekhov.core.models import Housing
from djchekhov.core.models import Registrar
from djchekhov.core.models import Services
from djchekhov.core.models import FINAID_CHOICES
from djchekhov.core.models import REGISTRATION_CHOICES
from djchekhov.core.models import GRADUATION_CHOICES
from djchekhov.core.models import ROOM_BOARD_CHOICES
from djchekhov.core.models import INSURANCE_CHOICES
from djchekhov.core.models import PARKING_PERMIT_CHOICES
from djchekhov.core.models import PAYMENT_CHOICES
from djchekhov.core.models import STUDENT_ID_CHOICES
from djtools.templatetags.livewhale_api import get_api_data


class AccountsForm(forms.ModelForm):
    """Form for the Student Accounts data model."""

    financial_aid = forms.ChoiceField(
        label="Financial Aid",
        help_text=get_api_data(3315)['body'],
        choices=FINAID_CHOICES,
        widget=forms.RadioSelect(),
    )
    rights_responsibilities = forms.BooleanField(
        label="Student Accounts",
        help_text=get_api_data(3317)['body'],
        required=True,
    )
    payment_plans = forms.ChoiceField(
        label="Payment Plans",
        help_text=get_api_data(3316)['body'],
        choices=PAYMENT_CHOICES,
        widget=forms.RadioSelect(),
    )

    class Meta:
        """Information about the data class model."""

        model = Accounts
        exclude = ('created_by', 'created_at', 'updated_at')


class ComplianceForm(forms.ModelForm):
    """Form for the data model."""

    community_code = forms.BooleanField(
        label="Community Code",
        help_text=get_api_data(3303)['body'],
        required=True,
    )
    sexual_misconduct = forms.BooleanField(
        label="Sexual Misconduct Policy",
        help_text=get_api_data(3304)['body'],
        required=True,
    )
    academic_honesty = forms.BooleanField(
        label="Academic Honesty Guidelines",
        help_text=get_api_data(3302)['body'],
        required=True,
    )

    class Meta:
        """Information about the data class model."""

        model = Compliance
        exclude = ('created_by', 'created_at', 'updated_at')


class EmergencyForm(forms.ModelForm):
    """Form for the data model."""

    emergency_contact = forms.BooleanField(
        label="Emergency Contact",
        help_text=get_api_data(3305)['body'],
        required=True,
    )
    insurance = forms.ChoiceField(
        label="International Student Insurance",
        help_text=get_api_data(3307)['body'],
        choices=INSURANCE_CHOICES,
        widget=forms.RadioSelect(),
    )

    class Meta:
        """Information about the data class model."""

        model = Emergency
        exclude = ('created_by', 'created_at', 'updated_at')


class HousingForm(forms.ModelForm):
    """Form for the data model."""

    room_board = forms.ChoiceField(
        label="Housing",
        help_text=get_api_data(3306)['body'],
        choices=ROOM_BOARD_CHOICES,
        widget=forms.RadioSelect(),
    )


    class Meta:
        """Information about the data class model."""

        model = Housing
        exclude = ('created_by', 'created_at', 'updated_at')


class RegistrarForm(forms.ModelForm):
    """Form for the data model."""

    email = forms.BooleanField(
        help_text=get_api_data(3308)['body'],
        required=True,
    )
    onelogin = forms.BooleanField(
        label="OneLogin",
        help_text=get_api_data(3311)['body'],
        required=True,
    )
    schoology = forms.BooleanField(
        help_text=get_api_data(3312)['body'],
        required=True,
    )
    registration = forms.ChoiceField(
        label="My Carthage Portal and Course Registration",
        help_text=get_api_data(3310)['body'],
        choices=REGISTRATION_CHOICES,
        widget=forms.RadioSelect(),
    )
    graduation = forms.ChoiceField(
        help_text=get_api_data(3309)['body'],
        choices=GRADUATION_CHOICES,
        widget=forms.RadioSelect(),
    )

    class Meta:
        """Information about the data class model."""

        model = Registrar
        exclude = ('created_by', 'created_at', 'updated_at')


class ServicesForm(forms.ModelForm):
    """Form for the data model."""

    parking_permit = forms.ChoiceField(
        label="Parking Permit",
        help_text=get_api_data(3313)['body'],
        choices=PARKING_PERMIT_CHOICES,
        widget=forms.RadioSelect(),
    )
    student_card = forms.ChoiceField(
        label="Student ID",
        help_text=get_api_data(3314)['body'],
        choices=STUDENT_ID_CHOICES,
        widget=forms.RadioSelect(),
    )


    class Meta:
        """Information about the data class model."""

        model = Services
        exclude = ('created_by', 'created_at', 'updated_at')
