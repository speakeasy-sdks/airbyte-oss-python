"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import privatesourcedefinitionread as shared_privatesourcedefinitionread
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class PrivateSourceDefinitionReadList:
    r"""Successful operation"""
    source_definitions: list[shared_privatesourcedefinitionread.PrivateSourceDefinitionRead] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceDefinitions') }})
    

