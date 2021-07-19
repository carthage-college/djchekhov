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


class AccountsForm(forms.ModelForm):
    """Form for the Student Accounts data model."""

    financial_aid = forms.ChoiceField(
        label="Fiancial Aid",
        help_text="""
        """,
        choices=FINAID_CHOICES,
        widget=forms.RadioSelect(),
    )
    rights_responsibilities = forms.BooleanField(
        label="I have read and agree to the rights and responsibilities.",
        required=True,
    )
    payment_plans = forms.ChoiceField(
        label="Payment Plans",
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
        label="""
            I have read the Community Code and understand that I am
            responsible for adhering to these policies as a
            Carthage College graduate student.
        """,
        required=True,
    )
    sexual_misconduct = forms.BooleanField(
        label="""
            I have read the Sexual Misconduct Policy and understand that I am
            responsible for adhering to these policies as a
            Carthage College graduate student. 
        """,
        required=True,
    )
    academic_honesty = forms.BooleanField(
        label="""
            I have read the Academic Honesty Policy and understand that I am
            responsible for adhering to these policies as a
            Carthage College graduate student. 
        """,
        required=True,
    )

    class Meta:
        """Information about the data class model."""

        model = Compliance
        exclude = ('created_by', 'created_at', 'updated_at')


class EmergencyForm(forms.ModelForm):
    """Form for the data model."""

    emergency_contact = forms.BooleanField(
        label="I have provided Emergency Contat Information.",
        required=True,
    )
    insurance = forms.ChoiceField(
        label="International Student Insurance",
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
        label="",
        choices=ROOM_BOARD_CHOICES,
        widget=forms.RadioSelect(),
    )


    class Meta:
        """Information about the data class model."""

        model = Housing
        exclude = ('created_by', 'created_at', 'updated_at')


class RegistrarForm(forms.ModelForm):
    """Form for the data model."""

    email = forms.BooleanField(required=True)
    onelogin = forms.BooleanField(label="OneLogin", required=True)
    schoology = forms.BooleanField(required=True)
    registration = forms.ChoiceField(
        label="Housing",
        choices=REGISTRATION_CHOICES,
        widget=forms.RadioSelect(),
    )
    graduation = forms.ChoiceField(
        label="Housing",
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
        choices=PARKING_PERMIT_CHOICES,
        widget=forms.RadioSelect(),
    )
    student_card = forms.ChoiceField(
        label="Student ID",
        choices=STUDENT_ID_CHOICES,
        widget=forms.RadioSelect(),
    )


    class Meta:
        """Information about the data class model."""

        model = Services
        exclude = ('created_by', 'created_at', 'updated_at')
