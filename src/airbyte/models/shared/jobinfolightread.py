"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import jobread as shared_jobread
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class JobInfoLightRead:
    r"""Successful operation"""
    
    job: shared_jobread.JobRead = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('job') }})
    