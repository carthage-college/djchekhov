# -*- coding: utf-8 -*-

"""Data models."""

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

from taggit.managers import TaggableManager

FINAID_CHOICES = (
    (
        'I have completed the required financial aid documents.',
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
REGISTRATION_CHOICES = (
    (
        '',
        "",
    ),
    (
        '',
        "",
    ),
)
GRADUATION_CHOICES = (
    (
        '',
        "",
    ),
    (
        '',
        "",
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
        '',
        "",
    ),
    (
        '',
        "",
    ),
)
PARKING_PERMIT_CHOICES = (
    (
        '',
        "",
    ),
    (
        '',
        "",
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
        on_delete=models.PROTECTED,
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
        related_name='finaid',
        editable=False,
        on_delete=models.PROTECTED,
    )
    created_at = models.DateTimeField("Date Created", auto_now_add=True)
    updated_at = models.DateTimeField("Date Updated", auto_now=True)
    financial_aid = models.CharField(max_length=128, choices=FINAID_CHOICES)
    rights_responsibilities = models.BooleanField(
        "I have read and agree to the rights and responsibilities.",
        default=False,
    )
    payment_option = models.CharField(max_length=128, choices=PAYMENT_CHOICES)


class Registrar(models.Model):
    """Office of the Registrar data."""

    manager = models.ForeignKey(
        Manager,
        related_name='registrar',
        editable=False,
        on_delete=models.PROTECTED,
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
        related_name='registrar',
        editable=False,
        on_delete=models.PROTECTED,
    )
    created_at = models.DateTimeField("Date Created", auto_now_add=True)
    updated_at = models.DateTimeField("Date Updated", auto_now=True)
    room_board = models.CharField(max_length=128, choices=ROOM_BOARD_CHOICES)


class Compliance(models.Model):
    """Documents that the student must sign."""

    manager = models.ForeignKey(
        Manager,
        related_name='registrar',
        editable=False,
        on_delete=models.PROTECTED,
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
        related_name='registrar',
        editable=False,
        on_delete=models.PROTECTED,
    )
    created_at = models.DateTimeField("Date Created", auto_now_add=True)
    updated_at = models.DateTimeField("Date Updated", auto_now=True)
    emergency_contact = models.BooleanField(default=False)
    insurance = models.CharField(max_length=128, choices=INSURANCE_CHOICES)


class Services(models.Model):
    """Student services."""

    manager = models.ForeignKey(
        Manager,
        related_name='registrar',
        editable=False,
        on_delete=models.PROTECTED,
    )
    created_at = models.DateTimeField("Date Created", auto_now_add=True)
    updated_at = models.DateTimeField("Date Updated", auto_now=True)
    parking_permit = models.CharField(max_length=128, choices=PARKING_PERMIT_CHOICES)
    student_card = models.CharField(
        "Student ID",
        max_length=128,
        choices=STUDENT_ID_CHOICES,
    )
