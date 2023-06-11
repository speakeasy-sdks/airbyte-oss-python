# WebBackendConnectionRead

Successful operation


## Fields

| Field                                                                                                                                                                                                                             | Type                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                       | Example                                                                                                                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `catalog_diff`                                                                                                                                                                                                                    | [Optional[CatalogDiff]](../../models/shared/catalogdiff.md)                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                | Describes the difference between two Airbyte catalogs.                                                                                                                                                                            |                                                                                                                                                                                                                                   |
| `catalog_id`                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                               |                                                                                                                                                                                                                                   |
| `connection_id`                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                               |                                                                                                                                                                                                                                   |
| `destination`                                                                                                                                                                                                                     | [DestinationRead](../../models/shared/destinationread.md)                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                               |                                                                                                                                                                                                                                   |
| `destination_id`                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                               |                                                                                                                                                                                                                                   |
| `geography`                                                                                                                                                                                                                       | [Optional[Geography]](../../models/shared/geography.md)                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                               |                                                                                                                                                                                                                                   |
| `is_syncing`                                                                                                                                                                                                                      | *bool*                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                               |                                                                                                                                                                                                                                   |
| `latest_sync_job_created_at`                                                                                                                                                                                                      | *Optional[int]*                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                | epoch time of the latest sync job. null if no sync job has taken place.                                                                                                                                                           |                                                                                                                                                                                                                                   |
| `latest_sync_job_status`                                                                                                                                                                                                          | [Optional[JobStatus]](../../models/shared/jobstatus.md)                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                               |                                                                                                                                                                                                                                   |
| `name`                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                               |                                                                                                                                                                                                                                   |
| `namespace_definition`                                                                                                                                                                                                            | [Optional[NamespaceDefinitionType]](../../models/shared/namespacedefinitiontype.md)                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                | Method used for computing final namespace in destination                                                                                                                                                                          |                                                                                                                                                                                                                                   |
| `namespace_format`                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                | Used when namespaceDefinition is 'customformat'. If blank then behaves like namespaceDefinition = 'destination'. If "${SOURCE_NAMESPACE}" then behaves like namespaceDefinition = 'source'.                                       | ${SOURCE_NAMESPACE}                                                                                                                                                                                                               |
| `non_breaking_changes_preference`                                                                                                                                                                                                 | [NonBreakingChangesPreference](../../models/shared/nonbreakingchangespreference.md)                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                               |                                                                                                                                                                                                                                   |
| `notify_schema_changes`                                                                                                                                                                                                           | *bool*                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                               |                                                                                                                                                                                                                                   |
| `operation_ids`                                                                                                                                                                                                                   | list[*str*]                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                               |                                                                                                                                                                                                                                   |
| `operations`                                                                                                                                                                                                                      | list[[OperationRead](../../models/shared/operationread.md)]                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                               |                                                                                                                                                                                                                                   |
| `prefix`                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                | Prefix that will be prepended to the name of each stream when it is written to the destination.                                                                                                                                   |                                                                                                                                                                                                                                   |
| `resource_requirements`                                                                                                                                                                                                           | [Optional[ResourceRequirements]](../../models/shared/resourcerequirements.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                | optional resource requirements to run workers (blank for unbounded allocations)                                                                                                                                                   |                                                                                                                                                                                                                                   |
| `schedule`                                                                                                                                                                                                                        | [Optional[ConnectionSchedule]](../../models/shared/connectionschedule.md)                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                | if null, then no schedule is set.                                                                                                                                                                                                 |                                                                                                                                                                                                                                   |
| `schedule_data`                                                                                                                                                                                                                   | [Optional[ConnectionScheduleData]](../../models/shared/connectionscheduledata.md)                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                | schedule for when the the connection should run, per the schedule type                                                                                                                                                            |                                                                                                                                                                                                                                   |
| `schedule_type`                                                                                                                                                                                                                   | [Optional[ConnectionScheduleType]](../../models/shared/connectionscheduletype.md)                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                | determine how the schedule data should be interpreted                                                                                                                                                                             |                                                                                                                                                                                                                                   |
| `schema_change`                                                                                                                                                                                                                   | [SchemaChange](../../models/shared/schemachange.md)                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                               |                                                                                                                                                                                                                                   |
| `source`                                                                                                                                                                                                                          | [SourceRead](../../models/shared/sourceread.md)                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                               |                                                                                                                                                                                                                                   |
| `source_id`                                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                | N/A                                                                                                                                                                                                                               |                                                                                                                                                                                                                                   |
| `status`                                                                                                                                                                                                                          | [ConnectionStatus](../../models/shared/connectionstatus.md)                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                                                                | Active means that data is flowing through the connection. Inactive means it is not. Deprecated means the connection is off and cannot be re-activated. the schema field describes the elements of the schema that will be synced. |                                                                                                                                                                                                                                   |
| `sync_catalog`                                                                                                                                                                                                                    | [AirbyteCatalog](../../models/shared/airbytecatalog.md)                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                | describes the available schema (catalog).                                                                                                                                                                                         |                                                                                                                                                                                                                                   |