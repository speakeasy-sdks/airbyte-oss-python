"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import invalidinputproperty as shared_invalidinputproperty
from airbyteoss import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class InvalidInputExceptionInfo:
    r"""Input failed validation"""
    
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    validation_errors: list[shared_invalidinputproperty.InvalidInputProperty] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validationErrors') }})
    exception_class_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('exceptionClassName'), 'exclude': lambda f: f is None }})
    exception_stack: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('exceptionStack'), 'exclude': lambda f: f is None }})
    