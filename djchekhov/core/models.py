# -*- coding: utf-8 -*-

"""Data models."""

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver

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
INSURANCE_CHOICES = (
    (
        'I am an international graduate student, and I understand that I will be billed for the cost of international student health insurance.',
        "I am an international graduate student, and I understand that I will be billed for the cost of international student health insurance.",
    ),
    (
        'I am an international graduate student TLE, and I understand that I will be provided with international student health insurance.',
        "I am an international graduate student TLE, and I understand that I will be provided with international student health insurance.",
    ),
    (
        'I am not an international student.',
        "I am not an international student.",
    ),
)
PARKING_PERMIT_CHOICES = (
    (
        'I plan to bring a vehicle to campus. I understand that I need to contact the Office of Public Safety at 262-551-5911 to register my vehicle and obtain the parking permit.',
        "I plan to bring a vehicle to campus. I understand that I need to contact the Office of Public Safety at 262-551-5911 to register my vehicle and obtain the parking permit.",
    ),
    (
        'I do not plan to bring a vehicle to campus at this time.',
        "I do not plan to bring a vehicle to campus at this time.",
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
    (
        'I will pay any remaining balance in full.',
        "I will pay any remaining balance in full.",
    ),
)

PROGRAM_CHOICES = (
    (
        'ACT/MED',
        "ACT/MED",
    ),
    (
        'Athletic Training',
        "Athletic Training",
    ),
    (
        'Business',
        "Business",
    ),
    (
        'Education',
        "Education",
    ),
    (
        'Music',
        "Music",
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
ROOM_BOARD_CHOICES = (
    (
        'I do not need graduate housing or a meal plan.',
        "I do not need graduate housing or a meal plan.",
    ),
    (
        'I do need graduate housing and/or a meal plan.',
        "I do need graduate housing and/or a meal plan.",
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


class Profile(models.Model):
    """Profile data class model for the graduate student check in."""

    user = models.OneToOneField(
        User,
        related_name='profile',
        #editable=False,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField("Date Created", auto_now_add=True)
    updated_at = models.DateTimeField("Date Updated", auto_now=True)
    program = models.CharField(max_length=128, choices=PROGRAM_CHOICES)

    class Meta:
        """Information about the data class model."""

        ordering  = ['-created_at']
        get_latest_by = 'created_at'

    def __str__(self):
        """Default data for display."""
        return "{0} ({1}): {2}".format(
            self.user.username,
            self.user.id,
            self.program,
        )

    def get_object(self, slug):
        """Return the object data."""
        current = None
        all_set = getattr(self.user, slug).all()
        if all_set:
            current = all_set.first()
        return current

    def accounts(self):
        """Return the student accounts data."""
        return self.get_object('accounts')

    def compliance(self):
        """Return the compliance data."""
        return self.get_object('compliance')

    def emergency(self):
        """Return the emergency contact and insurance data."""
        return self.get_object('emergency')

    def housing(self):
        """Return the housing data."""
        return self.get_object('housing')

    def registrar(self):
        """Return the registrar data."""
        return self.get_object('registrar')

    def services(self):
        """Return the student services data."""
        return self.get_object('services')


class Accounts(models.Model):
    """Student Accounts and Financial Aid."""

    user = models.ForeignKey(
        User,
        related_name='accounts',
        editable=False,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField("Date Created", auto_now_add=True)
    updated_at = models.DateTimeField("Date Updated", auto_now=True)
    financial_aid = models.CharField(max_length=128, choices=FINAID_CHOICES)
    rights_responsibilities = models.BooleanField(
        "I have read and agree to the rights and responsibilities.",
        default=False,
    )
    payment_plans = models.CharField(max_length=128, choices=PAYMENT_CHOICES)

    def __str__(self):
        """Default data for display."""
        return "{0} ({1})".format(
            self.user.username,
            self.user.id,
        )


class Compliance(models.Model):
    """Documents that the student must sign."""

    user = models.ForeignKey(
        User,
        related_name='compliance',
        editable=False,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField("Date Created", auto_now_add=True)
    updated_at = models.DateTimeField("Date Updated", auto_now=True)
    community_code = models.BooleanField(default=False)
    sexual_misconduct = models.BooleanField(default=False)
    academic_honesty = models.BooleanField(default=False)

    def __str__(self):
        """Default data for display."""
        return "{0} ({1})".format(
            self.user.username,
            self.user.id,
        )


class Emergency(models.Model):
    """ENS and health insurance."""

    user = models.ForeignKey(
        User,
        related_name='emergency',
        editable=False,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField("Date Created", auto_now_add=True)
    updated_at = models.DateTimeField("Date Updated", auto_now=True)
    emergency_contact = models.BooleanField(default=False)
    insurance = models.CharField(max_length=152, choices=INSURANCE_CHOICES)

    def __str__(self):
        """Default data for display."""
        return "{0} ({1})".format(
            self.user.username,
            self.user.id,
        )


class Housing(models.Model):
    """Housing and meal plans."""

    user = models.ForeignKey(
        User,
        related_name='housing',
        editable=False,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField("Date Created", auto_now_add=True)
    updated_at = models.DateTimeField("Date Updated", auto_now=True)
    room_board = models.CharField(max_length=128, choices=ROOM_BOARD_CHOICES)

    def __str__(self):
        """Default data for display."""
        return "{0} ({1})".format(
            self.user.username,
            self.user.id,
        )


class Registrar(models.Model):
    """Office of the Registrar data."""

    user = models.ForeignKey(
        User,
        related_name='registrar',
        editable=False,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField("Date Created", auto_now_add=True)
    updated_at = models.DateTimeField("Date Updated", auto_now=True)
    email = models.BooleanField(default=False)
    onelogin = models.BooleanField("OneLogin", default=False)
    schoology = models.BooleanField(default=False)
    registration = models.CharField(max_length=128, choices=REGISTRATION_CHOICES)
    graduation = models.CharField(max_length=128, choices=GRADUATION_CHOICES)

    def __str__(self):
        """Default data for display."""
        return "{0} ({1})".format(
            self.user.username,
            self.user.id,
        )


class Services(models.Model):
    """Student services."""

    user = models.ForeignKey(
        User,
        related_name='services',
        editable=False,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField("Date Created", auto_now_add=True)
    updated_at = models.DateTimeField("Date Updated", auto_now=True)
    parking_permit = models.CharField(max_length=192, choices=PARKING_PERMIT_CHOICES)
    student_card = models.CharField(
        "Student ID",
        max_length=128,
        choices=STUDENT_ID_CHOICES,
    )

    def __str__(self):
        """Default data for display."""
        return "{0} ({1})".format(
            self.user.username,
            self.user.id,
        )


@receiver(models.signals.post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Post-save signal function to create a user profile instance."""
    if created and not kwargs.get('raw', False):
        Profile.objects.create(user=instance)
