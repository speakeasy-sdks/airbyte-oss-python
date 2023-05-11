"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyteoss import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceCoreConfig:
    
    connection_configuration: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connectionConfiguration') }})
    r"""The values required to configure the source. The schema for this must match the schema return by source_definition_specifications/get for the source."""
    source_definition_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceDefinitionId') }})
    workspace_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workspaceId') }})
    source_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceId'), 'exclude': lambda f: f is None }})
    