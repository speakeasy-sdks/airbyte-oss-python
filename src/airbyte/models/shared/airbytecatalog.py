"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import airbytestreamandconfiguration as shared_airbytestreamandconfiguration
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AirbyteCatalog:
    r"""describes the available schema (catalog)."""
    
    streams: list[shared_airbytestreamandconfiguration.AirbyteStreamAndConfiguration] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('streams') }})
    