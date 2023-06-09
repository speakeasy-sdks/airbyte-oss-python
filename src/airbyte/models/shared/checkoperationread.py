"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class CheckOperationReadStatusEnum(str, Enum):
    SUCCEEDED = 'succeeded'
    FAILED = 'failed'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CheckOperationRead:
    r"""Successful operation"""
    
    status: CheckOperationReadStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    