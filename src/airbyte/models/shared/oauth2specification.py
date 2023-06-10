"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Any


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OAuth2Specification:
    r"""An object containing any metadata needed to describe this connector's Oauth flow"""
    oauth_flow_init_parameters: list[list[str]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('oauthFlowInitParameters') }})
    r"""Pointers to the fields in the rootObject needed to obtain the initial refresh/access tokens for the OAuth flow. Each inner array represents the path in the rootObject of the referenced field. For example. Assume the rootObject contains params 'app_secret', 'app_id' which are needed to get the initial refresh token. If they are not nested in the rootObject, then the array would look like this [['app_secret'], ['app_id']] If they are nested inside an object called 'auth_params' then this array would be [['auth_params', 'app_secret'], ['auth_params', 'app_id']]"""
    oauth_flow_output_parameters: list[list[str]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('oauthFlowOutputParameters') }})
    r"""Pointers to the fields in the rootObject which can be populated from successfully completing the oauth flow using the init parameters. This is typically a refresh/access token. Each inner array represents the path in the rootObject of the referenced field."""
    root_object: list[Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rootObject') }})
    r"""A list of strings representing a pointer to the root object which contains any oauth parameters in the ConnectorSpecification.
    Examples:
    if oauth parameters were contained inside the top level, rootObject=[] If they were nested inside another object {'credentials': {'app_id' etc...}, rootObject=['credentials'] If they were inside a oneOf {'switch': {oneOf: [{client_id...}, {non_oauth_param]}},  rootObject=['switch', 0]
    """
    

