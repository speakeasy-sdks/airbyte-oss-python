"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from airbyte.models import operations, shared
from typing import Optional

class Internal:
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests_http.Session, security_client: requests_http.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version
        
    
    def create_or_update_state(self, request: shared.ConnectionStateCreateOrUpdate) -> operations.CreateOrUpdateStateResponse:
        r"""Create or update the state for a connection."""
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/state/create_or_update'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateOrUpdateStateResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ConnectionState])
                res.connection_state = out
        elif http_res.status_code == 404:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.NotFoundKnownExceptionInfo])
                res.not_found_known_exception_info = out
        elif http_res.status_code == 422:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.InvalidInputExceptionInfo])
                res.invalid_input_exception_info = out

        return res

    
    def get_attempt_normalization_statuses_for_job(self, request: shared.JobIDRequestBody) -> operations.GetAttemptNormalizationStatusesForJobResponse:
        r"""Get normalization status to determine if we can bypass normalization phase"""
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/jobs/get_normalization_status'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        
        client = self._client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetAttemptNormalizationStatusesForJobResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.AttemptNormalizationStatusReadList])
                res.attempt_normalization_status_read_list = out

        return res

    
    def save_stats(self, request: shared.SaveStatsRequestBody) -> operations.SaveStatsResponse:
        r"""For worker to set sync stats of a running attempt."""
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/attempt/save_stats'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SaveStatsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.InternalOperationResult])
                res.internal_operation_result = out

        return res

    
    def save_sync_config(self, request: shared.SaveAttemptSyncConfigRequestBody) -> operations.SaveSyncConfigResponse:
        r"""For worker to save the AttemptSyncConfig for an attempt."""
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/attempt/save_sync_config'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SaveSyncConfigResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.InternalOperationResult])
                res.internal_operation_result = out

        return res

    
    def set_workflow_in_attempt(self, request: shared.SetWorkflowInAttemptRequestBody) -> operations.SetWorkflowInAttemptResponse:
        r"""For worker to register the workflow id in attempt."""
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/attempt/set_workflow_in_attempt'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.SetWorkflowInAttemptResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.InternalOperationResult])
                res.internal_operation_result = out

        return res

    
    def write_discover_catalog_result(self, request: shared.SourceDiscoverSchemaWriteRequestBody) -> operations.WriteDiscoverCatalogResultResponse:
        r"""Should only called from worker, to write result from discover activity back to DB."""
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/v1/sources/write_discover_catalog_result'
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        
        client = self._client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.WriteDiscoverCatalogResultResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.DiscoverCatalogResult])
                res.discover_catalog_result = out

        return res

    