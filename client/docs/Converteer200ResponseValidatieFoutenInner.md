# Converteer200ResponseValidatieFoutenInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**var_property** | **str** |  | [optional] 
**evaluation_path** | **str** |  | [optional] 
**schema_location** | **str** |  | [optional] 
**message_key** | **str** |  | [optional] 
**arguments** | **List[str]** |  | [optional] 

## Example

```python
from berichten_api.models.converteer200_response_validatie_fouten_inner import Converteer200ResponseValidatieFoutenInner

# TODO update the JSON string below
json = "{}"
# create an instance of Converteer200ResponseValidatieFoutenInner from a JSON string
converteer200_response_validatie_fouten_inner_instance = Converteer200ResponseValidatieFoutenInner.from_json(json)
# print the JSON string representation of the object
print(Converteer200ResponseValidatieFoutenInner.to_json())

# convert the object into a dict
converteer200_response_validatie_fouten_inner_dict = converteer200_response_validatie_fouten_inner_instance.to_dict()
# create an instance of Converteer200ResponseValidatieFoutenInner from a dict
converteer200_response_validatie_fouten_inner_from_dict = Converteer200ResponseValidatieFoutenInner.from_dict(converteer200_response_validatie_fouten_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


