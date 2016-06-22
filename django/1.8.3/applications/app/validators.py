#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -----------------------------------------------------
#  FileName    :    validators.py
#  Author      :    gaoyangqiming@
#  Project     :    hato/event
#  Date        :    2015-06-01
#  Description :    validators
# -----------------------------------------------------

from datetime import datetime
from django.utils.timezone import utc
from rest_framework import serializers


def utctimestamp_v(value):
    try:
        datetime.utcfromtimestamp(value).replace(tzinfo=utc)
    except Exception:
        raise serializers.ValidationError('not a utc timestamp')
