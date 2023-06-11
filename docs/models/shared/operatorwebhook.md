# OperatorWebhook


## Fields

| Field                                                                                     | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `dbt_cloud`                                                                               | [Optional[OperatorWebhookDbtCloud]](../../models/shared/operatorwebhookdbtcloud.md)       | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `execution_body`                                                                          | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | DEPRECATED. Populate dbtCloud instead.                                                    |
| `execution_url`                                                                           | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | DEPRECATED. Populate dbtCloud instead.                                                    |
| `webhook_config_id`                                                                       | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | The id of the webhook configs to use from the workspace.                                  |
| `webhook_type`                                                                            | [Optional[OperatorWebhookWebhookType]](../../models/shared/operatorwebhookwebhooktype.md) | :heavy_minus_sign:                                                                        | N/A                                                                                       |