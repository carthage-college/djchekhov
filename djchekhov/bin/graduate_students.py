#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import os
import sys

# env
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djchekhov.settings.shell')

# required if using django models
import django
django.setup()

from django.conf import settings
from django.contrib.auth.models import User

import argparse
import logging

logger = logging.getLogger('debug_logfile')

# set up command-line options
desc = """
Accepts as input a CSV file for user and profile data.
"""

# RawTextHelpFormatter method allows for new lines in help text
parser = argparse.ArgumentParser(
    description=desc, formatter_class=argparse.RawTextHelpFormatter,
)

parser.add_argument(
    '-f',
    '--file',
    required=True,
    help="Path to file",
    dest='phile',
)
parser.add_argument(
    '--test',
    action='store_true',
    help="Dry run?",
    dest='test',
)


def main():
    """Main function description."""
    with open(phile, 'r') as users:
        dialect = csv.Sniffer().sniff(users.read(1024 * 1024))
        users.seek(0)
        delimiter = dialect.delimiter
        reader = csv.DictReader(
            users, delimiter=delimiter, quoting=csv.QUOTE_NONE,
        )
        for row in reader:
            username = row['email'].split('@')[0]
            user, created = User.objects.get_or_create(
                id=row['id'],
                first_name=row['first_name'],
                last_name=row['last_name'],
                username=username,
                email=row['email'],
            )
            profile = user.profile
            profile.program=row['program']
            profile.save()
            print(created)


if __name__ == '__main__':
    args = parser.parse_args()
    phile = args.phile
    test = args.test

    if test:
        print(args)

    sys.exit(main())

