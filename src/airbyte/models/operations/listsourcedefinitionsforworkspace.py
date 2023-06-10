"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import sourcedefinitionreadlist as shared_sourcedefinitionreadlist
from typing import Optional



@dataclasses.dataclass
class ListSourceDefinitionsForWorkspaceResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    source_definition_read_list: Optional[shared_sourcedefinitionreadlist.SourceDefinitionReadList] = dataclasses.field(default=None)
    r"""Successful operation"""
    

