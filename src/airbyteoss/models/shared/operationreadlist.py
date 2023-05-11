"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import operationread as shared_operationread
from airbyteoss import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OperationReadList:
    r"""Successful operation"""
    
    operations: list[shared_operationread.OperationRead] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('operations') }})
    