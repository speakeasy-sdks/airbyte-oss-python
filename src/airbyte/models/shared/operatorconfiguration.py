"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import operatordbt as shared_operatordbt
from ..shared import operatornormalization as shared_operatornormalization
from ..shared import operatortype as shared_operatortype
from ..shared import operatorwebhook as shared_operatorwebhook
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OperatorConfiguration:
    
    operator_type: shared_operatortype.OperatorType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('operatorType') }})
    dbt: Optional[shared_operatordbt.OperatorDbt] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dbt'), 'exclude': lambda f: f is None }})
    normalization: Optional[shared_operatornormalization.OperatorNormalization] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('normalization'), 'exclude': lambda f: f is None }})
    webhook: Optional[shared_operatorwebhook.OperatorWebhook] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('webhook'), 'exclude': lambda f: f is None }})
    