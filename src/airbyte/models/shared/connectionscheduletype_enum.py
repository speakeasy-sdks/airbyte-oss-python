"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class ConnectionScheduleTypeEnum(str, Enum):
    r"""determine how the schedule data should be interpreted"""
    MANUAL = 'manual'
    BASIC = 'basic'
    CRON = 'cron'