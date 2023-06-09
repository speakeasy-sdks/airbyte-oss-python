# Airbyte SDK

## Overview

Airbyte Configuration API
[https://airbyte.io](https://airbyte.io).

This API is a collection of HTTP RPC-style methods. While it is not a REST API, those familiar with REST should find the conventions of this API recognizable.

Here are some conventions that this API follows:
* All endpoints are http POST methods.
* All endpoints accept data via `application/json` request bodies. The API does not accept any data via query params.
* The naming convention for endpoints is: localhost:8000/{VERSION}/{METHOD_FAMILY}/{METHOD_NAME} e.g. `localhost:8000/v1/connections/create`.
* For all `update` methods, the whole object must be passed in, even the fields that did not change.

Authentication (OSS):
* When authenticating to the Configuration API, you must use Basic Authentication by setting the Authentication Header to Basic and base64 encoding the username and password (which are `airbyte` and `password` by default - so base64 encoding `airbyte:password` results in `YWlyYnl0ZTpwYXNzd29yZA==`). So the full header reads `'Authorization': "Basic YWlyYnl0ZTpwYXNzd29yZA=="`


Find out more about Airbyte
<https://airbyte.io>
### Available Operations

