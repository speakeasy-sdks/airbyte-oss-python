"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import webbackendconnectionlistitem as shared_webbackendconnectionlistitem
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WebBackendConnectionReadList:
    r"""Successful operation"""
    
    connections: list[shared_webbackendconnectionlistitem.WebBackendConnectionListItem] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connections') }})
    