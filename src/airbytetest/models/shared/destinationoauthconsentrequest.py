"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbytetest import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationOauthConsentRequest:
    
    destination_definition_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationDefinitionId') }})
    redirect_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('redirectUrl') }})
    r"""The url to redirect to after getting the user consent"""
    workspace_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workspaceId') }})
    destination_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationId'), 'exclude': lambda f: f is None }})
    o_auth_input_configuration: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('oAuthInputConfiguration'), 'exclude': lambda f: f is None }})
    r"""The values required to configure OAuth flows. The schema for this must match the `OAuthConfigSpecification.oauthUserInputFromConnectorConfigSpecification` schema."""
    