"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import streamdescriptor as shared_streamdescriptor
from airbyteoss import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ResetConfig:
    r"""contains information about how a reset was configured. only populated if the job was a reset."""
    
    streams_to_reset: Optional[list[shared_streamdescriptor.StreamDescriptor]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('streamsToReset'), 'exclude': lambda f: f is None }})
    