"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import oauthconfigspecification as shared_oauthconfigspecification
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class AdvancedAuthAuthFlowType(str, Enum):
    OAUTH2_0 = 'oauth2.0'
    OAUTH1_0 = 'oauth1.0'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class AdvancedAuth:
    auth_flow_type: Optional[AdvancedAuthAuthFlowType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authFlowType'), 'exclude': lambda f: f is None }})
    oauth_config_specification: Optional[shared_oauthconfigspecification.OAuthConfigSpecification] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('oauthConfigSpecification'), 'exclude': lambda f: f is None }})
    predicate_key: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('predicateKey'), 'exclude': lambda f: f is None }})
    r"""Json Path to a field in the connectorSpecification that should exist for the advanced auth to be applicable."""
    predicate_value: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('predicateValue'), 'exclude': lambda f: f is None }})
    r"""Value of the predicate_key fields for the advanced auth to be applicable."""
    

