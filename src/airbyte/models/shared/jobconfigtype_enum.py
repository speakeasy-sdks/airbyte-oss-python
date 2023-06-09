"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class JobConfigTypeEnum(str, Enum):
    CHECK_CONNECTION_SOURCE = 'check_connection_source'
    CHECK_CONNECTION_DESTINATION = 'check_connection_destination'
    DISCOVER_SCHEMA = 'discover_schema'
    GET_SPEC = 'get_spec'
    SYNC = 'sync'
    RESET_CONNECTION = 'reset_connection'
