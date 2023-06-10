"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import attemptfailuresummary as shared_attemptfailuresummary
from ..shared import attemptstats as shared_attemptstats
from ..shared import attemptstatus as shared_attemptstatus
from ..shared import attemptstreamstats as shared_attemptstreamstats
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class AttemptRead:
    created_at: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt') }})
    id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    status: shared_attemptstatus.AttemptStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    updated_at: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt') }})
    bytes_synced: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bytesSynced'), 'exclude': lambda f: f is None }})
    ended_at: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('endedAt'), 'exclude': lambda f: f is None }})
    failure_summary: Optional[shared_attemptfailuresummary.AttemptFailureSummary] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('failureSummary'), 'exclude': lambda f: f is None }})
    records_synced: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recordsSynced'), 'exclude': lambda f: f is None }})
    stream_stats: Optional[list[shared_attemptstreamstats.AttemptStreamStats]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('streamStats'), 'exclude': lambda f: f is None }})
    total_stats: Optional[shared_attemptstats.AttemptStats] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalStats'), 'exclude': lambda f: f is None }})
    

