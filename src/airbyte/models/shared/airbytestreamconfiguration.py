"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import destinationsyncmode as shared_destinationsyncmode
from ..shared import selectedfieldinfo as shared_selectedfieldinfo
from ..shared import syncmode as shared_syncmode
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AirbyteStreamConfiguration:
    r"""the mutable part of the stream to configure the destination"""
    
    destination_sync_mode: shared_destinationsyncmode.DestinationSyncMode = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationSyncMode') }})
    sync_mode: shared_syncmode.SyncMode = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('syncMode') }})
    alias_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('aliasName'), 'exclude': lambda f: f is None }})
    r"""Alias name to the stream to be used in the destination"""
    cursor_field: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cursorField'), 'exclude': lambda f: f is None }})
    r"""Path to the field that will be used to determine if a record is new or modified since the last sync. This field is REQUIRED if `sync_mode` is `incremental`. Otherwise it is ignored."""
    field_selection_enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fieldSelectionEnabled'), 'exclude': lambda f: f is None }})
    r"""Whether field selection should be enabled. If this is true, only the properties in `selectedFields` will be included."""
    primary_key: Optional[list[list[str]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('primaryKey'), 'exclude': lambda f: f is None }})
    r"""Paths to the fields that will be used as primary key. This field is REQUIRED if `destination_sync_mode` is `*_dedup`. Otherwise it is ignored."""
    selected: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('selected'), 'exclude': lambda f: f is None }})
    r"""If this is true, the stream is selected with all of its properties. For new connections, this considers if the stream is suggested or not"""
    selected_fields: Optional[list[shared_selectedfieldinfo.SelectedFieldInfo]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('selectedFields'), 'exclude': lambda f: f is None }})
    r"""Paths to the fields that will be included in the configured catalog. This must be set if `fieldSelectedEnabled` is set. An empty list indicates that no properties will be included."""
    suggested: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('suggested'), 'exclude': lambda f: f is None }})
    r"""Does the connector suggest that this stream be enabled by default?"""
    