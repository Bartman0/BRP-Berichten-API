# PagineerbaarResultaat

Structuur bij responses die grotere data sets kunnen opleveren.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paginering** | [**PagineringResultaat**](PagineringResultaat.md) |  | 

## Example

```python
from berichten_api.models.pagineerbaar_resultaat import PagineerbaarResultaat

# TODO update the JSON string below
json = "{}"
# create an instance of PagineerbaarResultaat from a JSON string
pagineerbaar_resultaat_instance = PagineerbaarResultaat.from_json(json)
# print the JSON string representation of the object
print(PagineerbaarResultaat.to_json())

# convert the object into a dict
pagineerbaar_resultaat_dict = pagineerbaar_resultaat_instance.to_dict()
# create an instance of PagineerbaarResultaat from a dict
pagineerbaar_resultaat_from_dict = PagineerbaarResultaat.from_dict(pagineerbaar_resultaat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


