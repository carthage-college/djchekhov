# -*- coding: utf-8 -*-

"""Data models."""

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

FINAID_CHOICES = (
    (
        '''
        I have completed the required financial aid documents
        and submitted them to the Financial Aid Office.
        ''',
        """
        I have completed the required financial aid documents
        and submitted them to the Financial Aid Office.
        """,
    ),
    (
        'I am not receiving loans.',
        "I am not receiving loans.",
    ),
)
PAYMENT_CHOICES = (
    (
        'I plan to use the two-payment option above.',
        "I plan to use the two-payment option above.",
    ),
    (
        'I plan to use the monthly payment plan through ECSI.',
        "I plan to use the monthly payment plan through ECSI.",
    ),
)
REGISTRATION_CHOICES = (
    (
        'I have signed in to the My Carthage portal and my schedule is accurate.',
        "I have signed in to the My Carthage portal and my schedule is accurate.",
    ),
    (
        'I need assistance registering for my classes.',
        "I need assistance registering for my classes.",
    ),
)
GRADUATION_CHOICES = (
    (
        'I plan to graduate this academic year.',
        "I plan to graduate this academic year.",
    ),
    (
        'I do not plan to graduate this academic year.',
        "I do not plan to graduate this academic year.",
    ),
)
ROOM_BOARD_CHOICES = (
    (
        'I do not need graduate housing or a meal plan',
        "I do not need graduate housing or a meal plan",
    ),
    (
        'I do need graduate housing and/or a meal plan',
        "I do need graduate housing and/or a meal plan",
    ),
)
INSURANCE_CHOICES = (
    (
        '''
        I am an international graduate student, and I understand that I will be
        billed for the cost of international student health insurance.
        ''',
        """
        I am an international graduate student, and I understand that I will be
        billed for the cost of international student health insurance.
        """,
    ),
    (
        '''
        I am an international graduate student TLE, and I understand that
        I will be provided with international student health insurance.
        ''',
        """
        I am an international graduate student TLE, and I understand that
        I will be provided with international student health insurance.
        """,
    ),
    (
        'I am not an international student.',
        "I am not an international student.",
    ),
)
PARKING_PERMIT_CHOICES = (
    (
        '''
        I plan to bring a vehicle to campus. I understand that I need
        to contact the Office of Public Safety at 262-551-5911
        to register my vehicle and obtain the parking permit.
        ''',
        """
        I plan to bring a vehicle to campus. I understand that I need
        to contact the Office of Public Safety at 262-551-5911
        to register my vehicle and obtain the parking permit.
        """,
    ),
    (
        'I do not plan to bring a vehicle to campus at this time',
        "I do not plan to bring a vehicle to campus at this time",
    ),
)
STUDENT_ID_CHOICES = (
    (
        'I have updated my digital photo for my Carthage ID at the harbor link above.',
        "I have updated my digital photo for my Carthage ID at the harbor link above.",
    ),
    (
        'I need assistance taking and uploading a digital photo for my ID card.',
        "I need assistance taking and uploading a digital photo for my ID card.",
    ),
)


class Manager(models.Model):
    """Manager data class model for the graduate student check in."""

    created_by = models.ForeignKey(
        User,
        verbose_name='Created by',
        related_name='checkin',
        editable=False,
        on_delete=models.PROTECT,
    )
    created_at = models.DateTimeField("Date Created", auto_now_add=True)
    updated_at = models.DateTimeField("Date Updated", auto_now=True)

    class Meta:
        """Information about the data class model."""

        ordering  = ['-created_at']
        get_latest_by = 'created_at'

    def __str__(self):
        """Default data for display."""
        return self.created_by.username

    def get_absolute_url(self):
        """URL for the display view of the data class model."""
        return ('checkin_detail', [self.id])


class Accounts(models.Model):
    """Student Accounts and Financial Aid."""

    manager = models.ForeignKey(
        Manager,
        related_name='accounts',
        editable=False,
        on_delete=models.PROTECT,
    )
    created_at = models.DateTimeField("Date Created", auto_now_add=True)
    updated_at = models.DateTimeField("Date Updated", auto_now=True)
    rights_responsibilities = models.BooleanField(
        "I have read and agree to the rights and responsibilities.",
        default=False,
    )
    financial_aid = models.CharField(max_length=128, choices=FINAID_CHOICES)
    payment_plans = models.CharField(max_length=128, choices=PAYMENT_CHOICES)


class Registrar(models.Model):
    """Office of the Registrar data."""

    manager = models.ForeignKey(
        Manager,
        related_name='registrar',
        editable=False,
        on_delete=models.PROTECT,
    )
    created_at = models.DateTimeField("Date Created", auto_now_add=True)
    updated_at = models.DateTimeField("Date Updated", auto_now=True)
    email = models.BooleanField(default=False)
    onelogin = models.BooleanField("OneLogin", default=False)
    schoology = models.BooleanField(default=False)
    registration = models.CharField(max_length=128, choices=REGISTRATION_CHOICES)
    graduation = models.CharField(max_length=128, choices=GRADUATION_CHOICES)


class Housing(models.Model):
    """Housing and meal plans."""

    manager = models.ForeignKey(
        Manager,
        related_name='housing',
        editable=False,
        on_delete=models.PROTECT,
    )
    created_at = models.DateTimeField("Date Created", auto_now_add=True)
    updated_at = models.DateTimeField("Date Updated", auto_now=True)
    room_board = models.CharField(max_length=128, choices=ROOM_BOARD_CHOICES)


class Compliance(models.Model):
    """Documents that the student must sign."""

    manager = models.ForeignKey(
        Manager,
        related_name='compliance',
        editable=False,
        on_delete=models.PROTECT,
    )
    created_at = models.DateTimeField("Date Created", auto_now_add=True)
    updated_at = models.DateTimeField("Date Updated", auto_now=True)
    community_code = models.BooleanField(default=False)
    sexual_misconduct = models.BooleanField(default=False)
    academic_honesty = models.BooleanField(default=False)


class Emergency(models.Model):
    """ENS and health insurance."""

    manager = models.ForeignKey(
        Manager,
        related_name='emergency',
        editable=False,
        on_delete=models.PROTECT,
    )
    created_at = models.DateTimeField("Date Created", auto_now_add=True)
    updated_at = models.DateTimeField("Date Updated", auto_now=True)
    emergency_contact = models.BooleanField(default=False)
    insurance = models.CharField(max_length=128, choices=INSURANCE_CHOICES)


class Services(models.Model):
    """Student services."""

    manager = models.ForeignKey(
        Manager,
        related_name='services',
        editable=False,
        on_delete=models.PROTECT,
    )
    created_at = models.DateTimeField("Date Created", auto_now_add=True)
    updated_at = models.DateTimeField("Date Updated", auto_now=True)
    parking_permit = models.CharField(max_length=128, choices=PARKING_PERMIT_CHOICES)
    student_card = models.CharField(
        "Student ID",
        max_length=128,
        choices=STUDENT_ID_CHOICES,
    )
