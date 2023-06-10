"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import stateblob as shared_stateblob
from ..shared import streamdescriptor as shared_streamdescriptor
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class StreamState:
    stream_descriptor: shared_streamdescriptor.StreamDescriptor = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('streamDescriptor') }})
    stream_state: Optional[shared_stateblob.StateBlob] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('streamState'), 'exclude': lambda f: f is None }})
    

