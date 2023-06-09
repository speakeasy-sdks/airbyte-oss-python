"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import geography_enum as shared_geography_enum
from ..shared import notification as shared_notification
from ..shared import webhookconfigread as shared_webhookconfigread
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WorkspaceRead:
    r"""Successful operation"""
    
    customer_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerId') }})
    initial_setup_complete: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('initialSetupComplete') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    slug: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slug') }})
    workspace_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workspaceId') }})
    anonymous_data_collection: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('anonymousDataCollection'), 'exclude': lambda f: f is None }})
    default_geography: Optional[shared_geography_enum.GeographyEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('defaultGeography'), 'exclude': lambda f: f is None }})
    display_setup_wizard: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('displaySetupWizard'), 'exclude': lambda f: f is None }})
    email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email'), 'exclude': lambda f: f is None }})
    feedback_done: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('feedbackDone'), 'exclude': lambda f: f is None }})
    first_completed_sync: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('firstCompletedSync'), 'exclude': lambda f: f is None }})
    news: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('news'), 'exclude': lambda f: f is None }})
    notifications: Optional[list[shared_notification.Notification]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('notifications'), 'exclude': lambda f: f is None }})
    security_updates: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('securityUpdates'), 'exclude': lambda f: f is None }})
    webhook_configs: Optional[list[shared_webhookconfigread.WebhookConfigRead]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('webhookConfigs'), 'exclude': lambda f: f is None }})
    