"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import airbytecatalog as shared_airbytecatalog
from ..shared import connectionschedule as shared_connectionschedule
from ..shared import connectionscheduledata as shared_connectionscheduledata
from ..shared import connectionscheduletype as shared_connectionscheduletype
from ..shared import connectionstatus as shared_connectionstatus
from ..shared import geography as shared_geography
from ..shared import namespacedefinitiontype as shared_namespacedefinitiontype
from ..shared import nonbreakingchangespreference as shared_nonbreakingchangespreference
from ..shared import operationcreate as shared_operationcreate
from ..shared import resourcerequirements as shared_resourcerequirements
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class WebBackendConnectionCreate:
    destination_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationId') }})
    source_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceId') }})
    status: shared_connectionstatus.ConnectionStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""Active means that data is flowing through the connection. Inactive means it is not. Deprecated means the connection is off and cannot be re-activated. the schema field describes the elements of the schema that will be synced."""
    geography: Optional[shared_geography.Geography] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('geography'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Optional name of the connection"""
    namespace_definition: Optional[shared_namespacedefinitiontype.NamespaceDefinitionType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('namespaceDefinition'), 'exclude': lambda f: f is None }})
    r"""Method used for computing final namespace in destination"""
    namespace_format: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('namespaceFormat'), 'exclude': lambda f: f is None }})
    r"""Used when namespaceDefinition is 'customformat'. If blank then behaves like namespaceDefinition = 'destination'. If \\"${SOURCE_NAMESPACE}\\" then behaves like namespaceDefinition = 'source'."""
    non_breaking_changes_preference: Optional[shared_nonbreakingchangespreference.NonBreakingChangesPreference] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nonBreakingChangesPreference'), 'exclude': lambda f: f is None }})
    operation_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('operationIds'), 'exclude': lambda f: f is None }})
    operations: Optional[list[shared_operationcreate.OperationCreate]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('operations'), 'exclude': lambda f: f is None }})
    prefix: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prefix'), 'exclude': lambda f: f is None }})
    r"""Prefix that will be prepended to the name of each stream when it is written to the destination."""
    resource_requirements: Optional[shared_resourcerequirements.ResourceRequirements] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resourceRequirements'), 'exclude': lambda f: f is None }})
    r"""optional resource requirements to run workers (blank for unbounded allocations)"""
    schedule: Optional[shared_connectionschedule.ConnectionSchedule] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schedule'), 'exclude': lambda f: f is None }})
    r"""if null, then no schedule is set."""
    schedule_data: Optional[shared_connectionscheduledata.ConnectionScheduleData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scheduleData'), 'exclude': lambda f: f is None }})
    r"""schedule for when the the connection should run, per the schedule type"""
    schedule_type: Optional[shared_connectionscheduletype.ConnectionScheduleType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scheduleType'), 'exclude': lambda f: f is None }})
    r"""determine how the schedule data should be interpreted"""
    source_catalog_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceCatalogId'), 'exclude': lambda f: f is None }})
    sync_catalog: Optional[shared_airbytecatalog.AirbyteCatalog] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('syncCatalog'), 'exclude': lambda f: f is None }})
    r"""describes the available schema (catalog)."""
    

