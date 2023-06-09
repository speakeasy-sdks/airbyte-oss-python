"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import attemptfailurereason as shared_attemptfailurereason
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AttemptFailureSummary:
    
    failures: list[shared_attemptfailurereason.AttemptFailureReason] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('failures') }})
    partial_success: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('partialSuccess'), 'exclude': lambda f: f is None }})
    r"""True if the number of committed records for this attempt was greater than 0. False if 0 records were committed. If not set, the number of committed records is unknown."""
    