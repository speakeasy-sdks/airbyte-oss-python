"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import advancedauth as shared_advancedauth
from ..shared import destinationauthspecification as shared_destinationauthspecification
from ..shared import destinationsyncmode as shared_destinationsyncmode
from ..shared import synchronousjobread as shared_synchronousjobread
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DestinationDefinitionSpecificationRead:
    r"""Successful operation"""
    destination_definition_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationDefinitionId') }})
    job_info: shared_synchronousjobread.SynchronousJobRead = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jobInfo') }})
    advanced_auth: Optional[shared_advancedauth.AdvancedAuth] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('advancedAuth'), 'exclude': lambda f: f is None }})
    auth_specification: Optional[shared_destinationauthspecification.DestinationAuthSpecification] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authSpecification'), 'exclude': lambda f: f is None }})
    connection_specification: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connectionSpecification'), 'exclude': lambda f: f is None }})
    r"""The specification for what values are required to configure the destinationDefinition."""
    documentation_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('documentationUrl'), 'exclude': lambda f: f is None }})
    supported_destination_sync_modes: Optional[list[shared_destinationsyncmode.DestinationSyncMode]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('supportedDestinationSyncModes'), 'exclude': lambda f: f is None }})
    

