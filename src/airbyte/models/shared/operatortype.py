"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class OperatorType(str, Enum):
    NORMALIZATION = 'normalization'
    DBT = 'dbt'
    WEBHOOK = 'webhook'