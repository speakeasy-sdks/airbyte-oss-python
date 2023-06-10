"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import jobtyperesourcelimit as shared_jobtyperesourcelimit
from ..shared import resourcerequirements as shared_resourcerequirements
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ActorDefinitionResourceRequirements:
    r"""actor definition specific resource requirements. if default is set, these are the requirements that should be set for ALL jobs run for this actor definition. it is overriden by the job type specific configurations. if not set, the platform will use defaults. these values will be overriden by configuration at the connection level."""
    default: Optional[shared_resourcerequirements.ResourceRequirements] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('default'), 'exclude': lambda f: f is None }})
    r"""optional resource requirements to run workers (blank for unbounded allocations)"""
    job_specific: Optional[list[shared_jobtyperesourcelimit.JobTypeResourceLimit]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jobSpecific'), 'exclude': lambda f: f is None }})
    

