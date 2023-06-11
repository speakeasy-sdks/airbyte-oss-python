# NormalizationDestinationDefinitionConfig

describes a normalization config for destination definition


## Fields

| Field                                                                                                                                     | Type                                                                                                                                      | Required                                                                                                                                  | Description                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `normalization_integration_type`                                                                                                          | *Optional[str]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | a field indicating the type of integration dialect to use for normalization.                                                              |
| `normalization_repository`                                                                                                                | *Optional[str]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | a field indicating the name of the repository to be used for normalization. If the value of the flag is NULL - normalization is not used. |
| `normalization_tag`                                                                                                                       | *Optional[str]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | a field indicating the tag of the docker repository to be used for normalization.                                                         |
| `supported`                                                                                                                               | *bool*                                                                                                                                    | :heavy_check_mark:                                                                                                                        | whether the destination definition supports normalization.                                                                                |