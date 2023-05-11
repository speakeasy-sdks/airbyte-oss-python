"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyteoss import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSnippetRead:
    
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    source_definition_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceDefinitionId') }})
    source_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceId') }})
    source_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceName') }})
    icon: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('icon'), 'exclude': lambda f: f is None }})
    