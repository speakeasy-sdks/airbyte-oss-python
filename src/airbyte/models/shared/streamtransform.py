"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import fieldtransform as shared_fieldtransform
from ..shared import streamdescriptor as shared_streamdescriptor
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class StreamTransformTransformType(str, Enum):
    ADD_STREAM = 'add_stream'
    REMOVE_STREAM = 'remove_stream'
    UPDATE_STREAM = 'update_stream'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class StreamTransform:
    stream_descriptor: shared_streamdescriptor.StreamDescriptor = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('streamDescriptor') }})
    transform_type: StreamTransformTransformType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transformType') }})
    update_stream: Optional[list[shared_fieldtransform.FieldTransform]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updateStream'), 'exclude': lambda f: f is None }})
    r"""list of field transformations. order does not matter."""
    

