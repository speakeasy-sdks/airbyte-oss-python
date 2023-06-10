"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import fieldschema as shared_fieldschema
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class FieldSchemaUpdate:
    new_schema: shared_fieldschema.FieldSchema = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('newSchema') }})
    r"""JSONSchema representation of the field"""
    old_schema: shared_fieldschema.FieldSchema = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('oldSchema') }})
    r"""JSONSchema representation of the field"""
    

