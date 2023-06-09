"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import attemptread as shared_attemptread
from ..shared import logread as shared_logread
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AttemptInfoRead:
    
    attempt: shared_attemptread.AttemptRead = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attempt') }})
    logs: shared_logread.LogRead = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('logs') }})
    