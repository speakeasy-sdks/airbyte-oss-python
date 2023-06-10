"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import jobwithattemptsread as shared_jobwithattemptsread
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class JobReadList:
    r"""Successful operation"""
    jobs: list[shared_jobwithattemptsread.JobWithAttemptsRead] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jobs') }})
    total_job_count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('totalJobCount') }})
    r"""the total count of jobs for the specified connection"""
    

