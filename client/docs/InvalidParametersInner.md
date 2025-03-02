# InvalidParametersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from berichten_api.models.invalid_parameters_inner import InvalidParametersInner

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidParametersInner from a JSON string
invalid_parameters_inner_instance = InvalidParametersInner.from_json(json)
# print the JSON string representation of the object
print(InvalidParametersInner.to_json())

# convert the object into a dict
invalid_parameters_inner_dict = invalid_parameters_inner_instance.to_dict()
# create an instance of InvalidParametersInner from a dict
invalid_parameters_inner_from_dict = InvalidParametersInner.from_dict(invalid_parameters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


