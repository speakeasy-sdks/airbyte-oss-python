"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import destinationdefinitionreadlist as shared_destinationdefinitionreadlist
from typing import Optional



@dataclasses.dataclass
class ListDestinationDefinitionsForWorkspaceResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    destination_definition_read_list: Optional[shared_destinationdefinitionreadlist.DestinationDefinitionReadList] = dataclasses.field(default=None)
    r"""Successful operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

